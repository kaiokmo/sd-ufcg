import time

from monitor.monitor import Monitor

class Controller:
    def __init__(self, host):
        self.monitor = Monitor(host)

    def run(self):
        while True:
            status = self.monitor.check_status()
            print status
            time.sleep(5)

if __name__ == "__main__":
    controller = Controller("localhost:9090")
    controller.run()
