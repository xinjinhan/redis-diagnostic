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

    def evaluate_performance(self):
        start = time.time()
        self.redis.ping()
        end = time.time()
        return end - start  # 返回响应时间

    def objective(self, params):
        param_names = ['timeout', 'tcp-keepalive', 'maxclients', 'maxmemory', 'maxmemory-policy',
                       'hash-max-ziplist-entries', 'hash-max-ziplist-value', 'list-max-ziplist-size',
                       'zset-max-ziplist-entries', 'zset-max-ziplist-value']
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
            Integer(0, 10000, name='maxmemory'),
            Categorical(
                ['volatile-lru', 'allkeys-lru', 'volatile-random', 'allkeys-random', 'volatile-ttl', 'noeviction'],
                name='maxmemory-policy'),
            Integer(0, 512, name='hash-max-ziplist-entries'),
            Integer(0, 64, name='hash-max-ziplist-value'),
            Integer(0, 8, name='list-max-ziplist-size'),
            Integer(0, 128, name='zset-max-ziplist-entries'),
            Integer(0, 64, name='zset-max-ziplist-value')
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
