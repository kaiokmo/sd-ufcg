import time
import ConfigParser
import ast
import logging
import sys

from monitor.monitor import Monitor
import redis

class Controller:
    def __init__(self, clusters):
        redis_host = sys.argv[1]
        redis_port = sys.argv[2]
        self.redis = redis.Redis(host=redis_host, port=redis_port)
        self.monitors = []
        for cluster in clusters:
            addr = config.get(cluster, "address")
            logging.info("Updated configuration for cluster: " + cluster)
            self.monitors.append(Monitor(cluster, addr))

    def run(self):
        federated_metrics = {}
        while True:
            for monitor in self.monitors:
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


config = ConfigParser.ConfigParser()
config.read('controller.cfg')

if __name__ == "__main__":
    logging.basicConfig(filename='controller.log',level=logging.INFO)
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.info("Reading configuration file")
    config = ConfigParser.ConfigParser()
    config.read('controller.cfg')
    clusters = config.sections()
    controller = Controller(clusters)
    controller.run()
