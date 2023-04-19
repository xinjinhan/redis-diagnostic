import random


class RedisPerformanceDiagnosis:
    def __init__(self, **kwargs):
        self.memory_usage = kwargs.get('memory_usage', {'mean': 0, 'max': 0, 'min': 0})
        self.cache_hit_ratio = kwargs.get('cache_hit_ratio', {'mean': 0, 'max': 0, 'min': 0})
        self.connection_count = kwargs.get('connection_count', {'mean': 0, 'max': 0, 'min': 0})
        self.slow_query = kwargs.get('slow_query', {'mean': 0, 'max': 0, 'min': 0})
        self.cpu_usage = kwargs.get('cpu_usage', {'mean': 0, 'max': 0, 'min': 0})
        self.disk_usage = kwargs.get('disk_usage', {'mean': 0, 'max': 0, 'min': 0})
        self.bandwidth_usage = kwargs.get('bandwidth_usage', {'mean': 0, 'max': 0, 'min': 0})
        self.response_time = kwargs.get('response_time', {'mean': 0, 'max': 0, 'min': 0})
        self.client_buffer = kwargs.get('client_buffer', {'mean': 0, 'max': 0, 'min': 0})
        self.max_memory = kwargs.get('max_memory', 1024)
        self.max_bandwidth = kwargs.get('max_bandwidth', 10)
        self.slowlog_max_len = kwargs.get('slowlog_max_len', 128)
        self.server_cpu_cores = kwargs.get('server_cpu_cores', 8)
        self.client_buffer_peak_usage = kwargs.get('client_buffer_peak_usage', 1024)
        self.max_clients = kwargs.get('max_clients', 10000)
        self.min_memory_usage = kwargs.get('min_memory_usage', 0)
        self.min_cache_hit_ratio = kwargs.get('min_cache_hit_ratio', 0)
        self.min_connection_count = kwargs.get('min_connection_count', 0)
        self.min_slow_query = kwargs.get('min_slow_query', 0)
        self.min_cpu_usage = kwargs.get('min_cpu_usage', 0)
        self.min_disk_usage = kwargs.get('min_disk_usage', 0)
        self.min_bandwidth_usage = kwargs.get('min_bandwidth_usage', 0)
        self.min_response_time = kwargs.get('min_response_time', 0)
        self.min_client_buffer = kwargs.get('min_client_buffer', 0)

    def check_memory_usage(self):
        # 检查内存使用率是否超出限制
        if self.memory_usage['mean'] / self.max_memory >= 1:
            return 'Memory usage exceeds the limit. You should increase the memory limit.'
        else:
            return 'Memory usage is within the limit.'

    def check_cache_hit_ratio(self):
        # 检查缓存命中率是否低于阈值
        if self.cache_hit_ratio['mean'] <= 0.9:
            return 'Cache hit ratio is low. You should check your caching strategy.'
        else:
            return 'Cache hit ratio is good.'

    def check_connection_count(self):
        # 检查连接数是否超出限制
        if self.connection_count['mean'] >= self.max_clients:
            return 'Connection count exceeds the limit. You should increase the max clients limit.'
        else:
            return 'Connection count is within the limit.'

    def check_slow_query(self):
        # 检查慢查询数量是否超出限制
        if self.slow_query['max'] >= self.slowlog_max_len:
            return 'There are too many slow queries. You should optimize your queries or increase the slowlog max len.'
        else:
            return 'Slow query count is within the limit.'

    def check_cpu_usage(self):
        # 检查 CPU 使用率是否超出限制
        if self.cpu_usage['mean'] / self.server_cpu_cores >= 1:
            return 'CPU usage exceeds the limit. You should optimize your Redis configuration or upgrade your server.'
        else:
            return 'CPU usage is within the limit.'

    def check_disk_usage(self):
        # 检查磁盘使用率是否超出限制
        if self.disk_usage['mean'] / self.max_memory >= 1:
            return 'Disk usage exceeds the limit. You should increase the memory limit or clean up the disk.'
        else:
            return 'Disk usage is within the limit.'

    def check_bandwidth_usage(self):
        # 检查带宽使用率是否超出限制
        if self.bandwidth_usage['mean'] / self.max_bandwidth >= 1:
            return 'Bandwidth usage exceeds the limit. You should check your network connection.'
        else:
            return 'Bandwidth usage is within the limit.'

    def check_response_time(self):
        # 检查响应时间是否超出阈值
        if self.response_time['max'] >= 10:
            return 'Response time is slow. You should optimize your Redis configuration or network connection.'
        else:
            return 'Response time is good.'

    def check_client_buffer(self):
        # 检查客户端缓冲区使用率是否超出限制
        if self.client_buffer['mean'] / self.client_buffer_peak_usage >= 1:
            return 'Client buffer usage exceeds the limit. You should optimize your Redis configuration or client ' \
                   'application. '
        else:
            return 'Client buffer usage is within the limit.'


def preprocess_input_data(input_data):
    # 对输入数据进行预处理，包括计算平均值、最大值和最小值
    preprocessed_input_data = {}
    for key in input_data.keys():
        values = input_data[key]
        preprocessed_input_data[key] = {
            'mean': round(sum(values) / len(values), 2),
            'max': round(max(values), 2),
            'min': round(min(values), 2)
        }
    return preprocessed_input_data



def preprocess_input_data(input_data):
    # 对输入数据进行预处理，包括计算平均值、最大值和最小值
    mean_memory_usage = round(sum(input_data['memory_usage']) / len(input_data['memory_usage']), 2)
    max_memory_usage = round(max(input_data['memory_usage']), 2)
    min_memory_usage = round(min(input_data['memory_usage']), 2)
    mean_cache_hit_ratio = round(sum(input_data['cache_hit_ratio']) / len(input_data['cache_hit_ratio']), 2)
    max_cache_hit_ratio = round(max(input_data['cache_hit_ratio']), 2)
    min_cache_hit_ratio = round(min(input_data['cache_hit_ratio']), 2)
    mean_connection_count = round(sum(input_data['connection_count']) / len(input_data['connection_count']), 2)
    max_connection_count = round(max(input_data['connection_count']), 2)
    min_connection_count = round(min(input_data['connection_count']), 2)
    mean_slow_query = round(sum(input_data['slow_query']) / len(input_data['slow_query']), 2)
    max_slow_query = round(max(input_data['slow_query']), 2)
    min_slow_query = round(min(input_data['slow_query']), 2)
    mean_cpu_usage = round(sum(input_data['cpu_usage']) / len(input_data['cpu_usage']), 2)
    max_cpu_usage = round(max(input_data['cpu_usage']), 2)
    min_cpu_usage = round(min(input_data['cpu_usage']), 2)
    mean_disk_usage = round(sum(input_data['disk_usage']) / len(input_data['disk_usage']), 2)
    max_disk_usage = round(max(input_data['disk_usage']), 2)
    min_disk_usage = round(min(input_data['disk_usage']), 2)
    mean_bandwidth_usage = round(sum(input_data['bandwidth_usage']) / len(input_data['bandwidth_usage']), 2)
    max_bandwidth_usage = round(max(input_data['bandwidth_usage']), 2)
    min_bandwidth_usage = round(min(input_data['bandwidth_usage']), 2)
    mean_response_time = round(sum(input_data['response_time']) / len(input_data['response_time']), 2)
    max_response_time = round(max(input_data['response_time']), 2)
    min_response_time = round(min(input_data['response_time']), 2)
    mean_client_buffer = round(sum(input_data['client_buffer']) / len(input_data['client_buffer']), 2)
    max_client_buffer = round(max(input_data['client_buffer']), 2)
    min_client_buffer = round(min(input_data['client_buffer']), 2)

    return {
        'memory_usage': {'mean': mean_memory_usage, 'max': max_memory_usage, 'min': min_memory_usage},
        'cache_hit_ratio': {'mean': mean_cache_hit_ratio, 'max': max_cache_hit_ratio, 'min': min_cache_hit_ratio},
        'connection_count': {'mean': mean_connection_count, 'max': max_connection_count, 'min': min_connection_count},
        'slow_query': {'mean': mean_slow_query, 'max': max_slow_query, 'min': min_slow_query},
        'cpu_usage': {'mean': mean_cpu_usage, 'max': max_cpu_usage, 'min': min_cpu_usage},
        'disk_usage': {'mean': mean_disk_usage, 'max': max_disk_usage, 'min': min_disk_usage},
        'bandwidth_usage': {'mean': mean_bandwidth_usage, 'max': max_bandwidth_usage, 'min': min_bandwidth_usage},
        'response_time': {'mean': mean_response_time, 'max': max_response_time, 'min': min_response_time},
        'client_buffer': {'mean': mean_client_buffer, 'max': max_client_buffer, 'min': min_client_buffer},
    }


if __name__ == '__main__':
    # 输入数据示例
    input_data = {
        'memory_usage': [800, 850, 1000, 900, 950],
        'cache_hit_ratio': [0.8, 0.7, 0.9, 0.8, 0.85],
        'connection_count': [200, 180, 220, 210, 190],
        'slow_query': [10, 8, 12, 11, 9],
        'cpu_usage': [0.5, 0.6, 0.4, 0.5, 0.55],
        'disk_usage': [0.3, 0.35, 0.25, 0.3, 0.3],
        'bandwidth_usage': [8, 7, 9, 8, 8.5],
        'response_time': [1.2, 1.5, 1.0, 1.1, 1.3],
        'client_buffer': [500, 550, 600, 650, 700]
    }

    # Redis 参数值
    redis_config = {
        'max_memory': 1024,
        'max_bandwidth': 10,
        'client_buffer_peak_usage': 1024,
        'max_clients': 10000,
        'slowlog_max_len': 128,
        'min_memory_usage': 0,
        'min_cache_hit_ratio': 0,
        'min_connection_count': 0,
        'min_slow_query': 0,
        'min_cpu_usage': 0,
        'min_disk_usage': 0,
        'min_bandwidth_usage': 0,
        'min_response_time': 0,
        'min_client_buffer': 0
    }

    # 合并redis性能指标与配置参数
    input_data.update(redis_config)

    # 预处理输入数据
    preprocessed_input_data = preprocess_input_data(input_data)

    # 创建 RedisPerformanceDiagnosis 实例
    diagnosis = RedisPerformanceDiagnosis(**preprocessed_input_data)

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
