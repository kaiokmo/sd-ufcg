import time
import ConfigParser
import ast
import logging

from monitor.monitor import Monitor

class Controller:
    def __init__(self, clusters):
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
            logging.info(federated_metrics)

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
