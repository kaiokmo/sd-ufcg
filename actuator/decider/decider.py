# -*- coding: utf-8 -*-
""" module decider
        decicdes over received metrics.
"""

from kubernetes import client, config

class Decider(object):
    """ class Decider
        encapsulates tolerance and decision parameters.
    """
    def __init__(self, tolerance, max_size, context, application, init_size):
        config.load_kube_config(context=context)
        self._context = context
        self._tolerance = float(tolerance)
        self._max_size = max_size
        self._api = client.ExtensionsV1beta1Api()
        self._application = application
        self._init_size = float(init_size)

    @property
    def tolerance(self):
        """ tolerance()
            return saved tolerance.
        """
        return self._tolerance

    def _replication(self):
        return self._api.read_namespaced_deployment(
            name=self._application,
            namespace="default"
        ).spec.replicas

    def _deployment(self):
        return self._api.read_namespaced_deployment(
            name=self._application,
            namespace="default"
        )
    
    def _scale(self):
        replication = self._replication()
        if replication >= self._max_size:
            pass
        print "scaling from %d to %d" % (replication, replication + 1)
        deployment = self._deployment()
        deployment.spec.replicas = replication + 1
        self._api.patch_namespaced_deployment(
            name=self._application,
            namespace="default",
            body=deployment
        )
        print "current: %d" % self._replication()

    def _drop(self):
        deployment = self._deployment()
        print "for %s: %d" % (self._context, deployment.spec.replicas)
        if deployment.spec.replicas != self._init_size:
            deployment.spec.replicas = self._init_size
            self._api.patch_namespaced_deployment(
                name=self._application,
                namespace="default",
                body=deployment
            )

    def process_metric(self, metric):
        """ process_metric(metric)
                analyses passed metric and deccides workload balancing.
        """
        marked = 0
        for node in metric:
            if node >= self._tolerance:
                marked += 1
        print "marked nodes: %d" % marked
        if marked == self._replication():
            self._scale()
        elif marked == 0:
            self._drop()
