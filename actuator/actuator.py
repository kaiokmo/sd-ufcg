# -*- coding: utf-8 -*-
""" module actuator
        collects metrics and analyses.
"""
import ConfigParser
import logging
import time
import json

from collector.collector import Collector
from decider.decider import Decider

logging.basicConfig(filename='actuator.log', level=logging.INFO)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.info("Reading configuration file")
CONFIG = ConfigParser.ConfigParser()
CONFIG.read('actuator.cfg')
REDIS_HOST = CONFIG.get("REDIS", "address")
REDIS_PORT = CONFIG.get("REDIS", "port")
TOLERANCE = CONFIG.get("ACTUATION", "tolerance")
MAX_SIZE = CONFIG.get("ACTUATION", "max_size")
INIT_SIZE = CONFIG.get("ACTUATION", "init_size")
CONTEXTS = CONFIG.get("FEDERATION", "contexts").split(",")
APPLICATION = CONFIG.get("FEDERATION", "application")
COLLECTOR = Collector(redis_host=REDIS_HOST, redis_port=REDIS_PORT)
DECIDERS = {}
for context in CONTEXTS:
    DECIDERS[context] = Decider(
        tolerance=TOLERANCE,
        max_size=MAX_SIZE,
        context=context,
        application=APPLICATION,
        init_size=INIT_SIZE
    )


while True:
    METRIC = COLLECTOR.collect_recent()
    x = json.loads(METRIC[1].replace("'", '"'))
    for context_metric in x:
        DECIDERS[context_metric].process_metric(x[context_metric])
    time.sleep(7)
