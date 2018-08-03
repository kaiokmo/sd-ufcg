class Monitor:
    def __init__(self, host):
        self.endpoint = """
            http://%s/api/v1/query?query=1%20-%20avg%20by(instance)(irate(node_cpu{mode=%27idle%27}[5m]))
        """ % host

    def check_status(self):
        pass

