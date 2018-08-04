# -*- coding: utf-8 -*-
""" Module monitor
        queries cluter status and return.
"""
import requests

class Monitor(object):
    """ Class Monitor
            monitors a cluster and return its data.
    """
    def __init__(self, name, host):
        self.name = name
        self.endpoint = "http://{0}/api/v1/query?query=avg%20by(instance){1}".format(
            host,
            "(irate(node_cpu{mode='idle'}[5m]))"
        )

    @property
    def endpoint(self):
        """ endpoint()
                return the prometheus endpoint used.
        """
        return self.endpoint

    def check_status(self):
        """ check_status()
                return cpu data from prometheus server.
        """
        data = requests.get(self.endpoint).json()
        metrics = []
        for node in data['data']['result']:
            metrics.append(1 - float(node['value'][1]))
        return (self.name, metrics)
