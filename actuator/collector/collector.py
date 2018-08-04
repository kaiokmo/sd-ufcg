# -*- coding: utf-8 -*-
""" module collector
        collects saved metrics and returns.
"""
import redis

class Collector(object):
    """ class Collector()
            collects metrics from redis.
    """
    def __init__(self, redis_host, redis_port):
        self._queue = "federated:metrics"
        self.redis = redis.Redis(host=redis_host, port=redis_port)

    @property
    def queue(self):
        """ queue()
            returns queue used to collect metrics.
        """
        return self._queue

    def collect_recent(self):
        """ collect_recent()
                return most recent metrics.
        """
        return self.redis.blpop(self._queue)
