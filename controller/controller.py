# -*- coding: utf-8 -*-
"""Controller module
    Monitor the federation cpu usage and
        publish all colected metrics to a
        redis queue.

    Run:
        $ python controller.py ip port
"""
import time
import ConfigParser
import logging
import sys

import redis
from monitor.monitor import Monitor

class Controller(object):
    """Class controller:
        Saves redis address and loads each cluster monitor."""
    def __init__(self, federated_clusters):
        redis_host = sys.argv[1]
        redis_port = sys.argv[2]
        self.redis = redis.Redis(host=redis_host, port=redis_port)
        self._monitors = []
        for cluster in federated_clusters:
            addr = CONFIG.get(cluster, "address")
            logging.info("Updated configuration for cluster: %s", cluster)
            self._monitors.append(Monitor(cluster, addr))

    @property
    def monitors(self):
        """monitors()
            return all monitor instances
        """
        return self._monitors

    def run(self):
        """run():
            starts monitoring all clusters.
        """
        federated_metrics = {}
        while True:
            for monitor in self._monitors:
                status = monitor.check_status()
                federated_metrics[status[0]] = status[1]
            time.sleep(5)
            self._publish_metrics(federated_metrics)
            logging.info(federated_metrics)

    def _publish_metrics(self, json):
        self.redis.lpush(
            "federated:metrics",
            json
        )


CONFIG = ConfigParser.ConfigParser()
CONFIG.read('controller.cfg')

if __name__ == "__main__":
    logging.basicConfig(filename='controller.log', level=logging.INFO)
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.info("Reading configuration file")
    CLUSTERS = CONFIG.sections()
    CONTROLLER = Controller(CLUSTERS)
    CONTROLLER.run()
