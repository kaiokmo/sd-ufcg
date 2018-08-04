# -*- coding: utf-8 -*-
""" module actuator
        collects metrics and analyses.
"""
import ConfigParser
import logging
import time

from collector.collector import Collector

logging.basicConfig(filename='actuator.log', level=logging.INFO)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.info("Reading configuration file")
CONFIG = ConfigParser.ConfigParser()
CONFIG.read('actuator.cfg')
REDIS_HOST = CONFIG.get("REDIS", "address")
REDIS_PORT = CONFIG.get("REDIS", "port")
COLLECTOR = Collector(REDIS_HOST, REDIS_PORT)


while True:
    METRIC = COLLECTOR.collect_recent()
    print METRIC
    time.sleep(7)
