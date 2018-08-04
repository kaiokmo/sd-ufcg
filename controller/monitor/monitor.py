import requests
import json

import prometheus_client

class Monitor:
    def __init__(self, name, host):
        self.name = name
        self.endpoint = "http://{0}/api/v1/query?query=avg%20by(instance){1}".format(
            host,
            "(irate(node_cpu{mode='idle'}[5m]))"
        )

    def check_status(self):
        data = requests.get(self.endpoint).json()
        metrics = []
        for node in data['data']['result']:
            metrics.append(1 - float(node['value'][1]))
        return (self.name, metrics)
