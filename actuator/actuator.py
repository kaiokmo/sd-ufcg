import ConfigParser
import logging
import time

from collector.collector import Collector

logging.basicConfig(filename='actuator.log',level=logging.INFO)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.info("Reading configuration file")
config = ConfigParser.ConfigParser()
config.read('actuator.cfg')
redis_host = config.get("REDIS", "address")
redis_port = config.get("REDIS", "port")
collector = Collector(redis_host, redis_port)


while True:
    metric = collector.collect_recent()
    print metric
    time.sleep(7)