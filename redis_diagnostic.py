import asyncio
import json
import random


class RedisPerformanceDiagnosis:
    def __init__(self, memory_usage, cache_hit_ratio, connection_count, slow_query, cpu_usage, disk_usage,
                 bandwidth_usage, response_time, client_buffer, **kwargs):
        # 初始化 Redis 性能指标的值
        self.memory_usage = memory_usage
        self.cache_hit_ratio = cache_hit_ratio
        self.connection_count = connection_count
        self.slow_query = slow_query
        self.cpu_usage = cpu_usage
        self.disk_usage = disk_usage
        self.bandwidth_usage = bandwidth_usage
        self.response_time = response_time
        self.client_buffer = client_buffer
        # 初始化 Redis 实例的其他配置参数
        self.max_memory = kwargs.get('max_memory', 1)
        self.max_clients = kwargs.get('max_clients', 1)
        self.slowlog_max_len = kwargs.get('slowlog_max_len', 1)
        self.server_cpu_cores = kwargs.get('server_cpu_cores', 1)
        self.max_bandwidth = kwargs.get('max_bandwidth', 1)
        self.client_buffer_peak_usage = kwargs.get('client_buffer_peak_usage', 1)

    def check_memory_usage(self):
        # 检查内存使用率是否超出限制
        if self.memory_usage / self.max_memory >= 1:
            return 'Memory usage exceeds the limit. You should increase the memory limit.'
        else:
            return 'Memory usage is within the limit.'

    def check_cache_hit_ratio(self):
        # 检查缓存命中率是否低于阈值
        if self.cache_hit_ratio <= 0.9:
            return 'Cache hit ratio is low. You should check your caching strategy.'
        else:
            return 'Cache hit ratio is good.'

    def check_connection_count(self):
        # 检查连接数是否超出限制
        if self.connection_count >= self.max_clients:
            return 'Connection count exceeds the limit. You should increase the max clients limit.'
        else:
            return 'Connection count is within the limit.'

    def check_slow_query(self):
        # 检查慢查询数量是否超出限制
        if max(self.slow_query) >= self.slowlog_max_len:
            return 'There are too many slow queries. You should optimize your queries or increase the slowlog max len.'
        else:
            return 'Slow query count is within the limit.'

    def check_cpu_usage(self):
        # 检查 CPU 使用率是否超出限制
        if self.cpu_usage / self.server_cpu_cores >= 1:
            return 'CPU usage exceeds the limit. You should optimize your Redis configuration or upgrade your server.'
        else:
            return 'CPU usage is within the limit.'

    def check_disk_usage(self):
        # 检查磁盘使用率是否超出限制
        if self.disk_usage / self.max_memory >= 1:
            return 'Disk usage exceeds the limit. You should increase the memory limit or clean up the disk.'
        else:
            return 'Disk usage is within the limit.'

    def check_bandwidth_usage(self):
        # 检查带宽使用率是否超出限制
        if self.bandwidth_usage / self.max_bandwidth >= 1:
            return 'Bandwidth usage exceeds the limit. You should check your network connection.'
        else:
            return 'Bandwidth usage is within the limit.'

    def check_response_time(self):
        # 检查响应时间是否超出阈值
        if max(self.response_time) >= 10:
            return 'Response time is slow. You should optimize your Redis configuration or network connection.'
        else:
            return 'Response time is good.'

    def check_client_buffer(self):
        # 检查客户端缓冲区使用率是否超出限制
        if self.client_buffer / self.client_buffer_peak_usage >= 1:
            return 'Client buffer usage exceeds the limit. You should optimize your Redis configuration or client application.'
        else:
            return 'Client buffer usage is within the limit.'


if __name__ == '__main__':
    # 随机生成指标值
    memory_usage = random.randint(100, 500)
    cache_hit_ratio = random.uniform(0.8, 1)
    connection_count = random.randint(500, 2000)
    slow_query = [random.randint(1, 10) for i in range(5)]
    cpu_usage = random.uniform(1, 3)
    disk_usage = random.randint(200, 800)
    bandwidth_usage = random.uniform(1, 10)
    response_time = [random.randint(1, 10) for i in range(5)]
    client_buffer = random.randint(500, 1500)

    # 随机生成一些额外参数
    max_memory = random.randint(500, 1000)
    max_clients = random.randint(2000, 5000)
    slowlog_max_len = random.randint(5, 20)
    server_cpu_cores = random.randint(2, 8)
    max_bandwidth = random.uniform(5, 20)
    client_buffer_peak_usage = random.randint(1000, 3000)

    # 创建 RedisPerformanceDiagnosis 实例
    diagnosis = RedisPerformanceDiagnosis(
        memory_usage=memory_usage,
        cache_hit_ratio=cache_hit_ratio,
        connection_count=connection_count,
        slow_query=slow_query,
        cpu_usage=cpu_usage,
        disk_usage=disk_usage,
        bandwidth_usage=bandwidth_usage,
        response_time=response_time,
        client_buffer=client_buffer,
        max_memory=max_memory,
        max_clients=max_clients,
        slowlog_max_len=slowlog_max_len,
        server_cpu_cores=server_cpu_cores,
        max_bandwidth=max_bandwidth,
        client_buffer_peak_usage=client_buffer_peak_usage
    )

    # 进行性能诊断
    diagnosis_results = [
        diagnosis.check_memory_usage(),
        diagnosis.check_cache_hit_ratio(),
        diagnosis.check_connection_count(),
        diagnosis.check_slow_query(),
        diagnosis.check_cpu_usage(),
        diagnosis.check_disk_usage(),
        diagnosis.check_bandwidth_usage(),
        diagnosis.check_response_time(),
        diagnosis.check_client_buffer(),
    ]

    # 输出诊断结果
    for result in diagnosis_results:
        print(result)
