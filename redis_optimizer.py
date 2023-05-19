import redis
import time
import pandas as pd
import matplotlib.pyplot as plt
from skopt import gp_minimize
from skopt.space import Real, Integer, Categorical

class RedisOptimizer:
    def __init__(self, redis_host, redis_port):
        self.redis = redis.Redis(host=redis_host, port=redis_port)
        self.history = pd.DataFrame(columns=['params', 'performance'])

    def evaluate_response_time(self):
        start = time.time()
        self.redis.ping()
        end = time.time()
        return end - start  # 返回响应时间

    def evaluate_latency(self):
        latency = self.redis.execute_command('LATENCY LATEST')
        return latency[0][2] if latency else 0  # 返回最新的延迟值

    def evaluate_throughput(self):
        start = time.time()
        for _ in range(1000):
            self.redis.ping()
        end = time.time()
        return 1000 / (end - start)  # 返回吞吐量（每秒查询数）

    def evaluate_cache_hit_rate(self):
        stats = self.redis.info('stats')
        hits = stats['keyspace_hits']
        misses = stats['keyspace_misses']
        return hits / (hits + misses) if hits + misses > 0 else 0  # 返回缓存命中率

    def objective(self, params):
        param_names = ['timeout', 'tcp-keepalive', 'maxclients', 'maxmemory-policy',
                       'hash-max-ziplist-entries', 'hash-max-ziplist-value', 'list-max-ziplist-size',
                       'zset-max-ziplist-entries', 'zset-max-ziplist-value', 'hash-max-ziplist-entries-cpu',
                       'hash-max-ziplist-value-cpu']
        params_dict = dict(zip(param_names, params))

        for name, value in params_dict.items():
            self.redis.config_set(name, value)

        performance = self.evaluate_performance()
        self.history = self.history.append({'params': params_dict, 'performance': performance}, ignore_index=True)

        return performance

    def optimize(self, n_calls=100):
        space = [
            Integer(0, 60, name='timeout'),
            Integer(0, 300, name='tcp-keepalive'),
            Integer(1, 10000, name='maxclients'),
            Categorical(
                ['volatile-lru', 'allkeys-lru', 'volatile-random', 'allkeys-random', 'volatile-ttl', 'noeviction'],
                name='maxmemory-policy'),
            Integer(0, 512, name='hash-max-ziplist-entries'),
            Integer(0, 64, name='hash-max-ziplist-value'),
            Integer(0, 8, name='list-max-ziplist-size'),
            Integer(0, 128, name='zset-max-ziplist-entries'),
            Integer(0, 64, name='zset-max-ziplist-value'),
            # 添加CPU相关的参数
            Integer(1, 100, name='hash-max-ziplist-entries'),
            Integer(1, 100, name='hash-max-ziplist-value')
        ]
        res = gp_minimize(self.objective, space, n_calls=n_calls)
        return res

    def plot_history(self):
        self.history['performance'].plot()
        plt.show()

# 使用方法：
# optimizer = RedisOptimizer('localhost', 6379)
# optimizer.optimize()
# optimizer.plot_history()
