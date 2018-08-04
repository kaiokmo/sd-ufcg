import redis

class Collector:
    def __init__(self, redis_host, redis_port):
        self.redis = redis.Redis(host=redis_host, port=redis_port)
    
    def collect_recent(self):
        return self.redis.blpop("federated:metrics")
