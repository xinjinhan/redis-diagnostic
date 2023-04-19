import unittest
from decimal import Decimal

from redis_diagnostic import RedisPerformanceDiagnosis, preprocess_input_data


class TestRedisPerformanceDiagnosis(unittest.TestCase):

    def setUp(self):
        # 示例 Redis 配置参数
        config = {
            'max_memory': 1024,
            'max_bandwidth': 10,
            'client_buffer_peak_usage': 1024,
            'min_memory_usage': 0,
            'min_cache_hit_ratio': 0,
            'min_connection_count': 0,
            'min_slow_query': 0,
            'min_cpu_usage': 0,
            'min_disk_usage': 0,
            'min_bandwidth_usage': 0,
            'min_response_time': 0,
            'min_client_buffer': 0,
        }

        # 示例输入数据
        input_data = {
            'memory_usage': [250, 300, 280, 270, 290],
            'cache_hit_ratio': [0.92, 0.95, 0.89, 0.91, 0.93],
            'connection_count': [1000, 1200, 900, 1100, 1000],
            'slow_query': [1, 2, 3, 4, 5],
            'cpu_usage': [2.5, 3.0, 2.8, 2.7, 2.9],
            'disk_usage': [500, 550, 520, 530, 540],
            'bandwidth_usage': [5, 6, 4, 5, 5],
            'response_time': [5, 6, 7, 8, 9],
            'client_buffer': [1000, 1200, 900, 1000, 1100],
        }
        preprocessed_input_data = preprocess_input_data(input_data)
        self.diagnosis = RedisPerformanceDiagnosis(**preprocessed_input_data, **config)

    def test_check_memory_usage(self):
        result = self.diagnosis.check_memory_usage()
        self.assertEqual(result, 'Memory usage is within the limit.')

    def test_check_cache_hit_ratio(self):
        result = self.diagnosis.check_cache_hit_ratio()
        self.assertEqual(result, 'Cache hit ratio is good.')

    def test_check_connection_count(self):
        result = self.diagnosis.check_connection_count()
        self.assertEqual(result, 'Connection count is within the limit.')

    def test_check_slow_query(self):
        result = self.diagnosis.check_slow_query()
        self.assertEqual(result, 'Slow query count is within the limit.')

    def test_check_cpu_usage(self):
        result = self.diagnosis.check_cpu_usage()
        self.assertEqual(result, 'CPU usage is within the limit.')

    def test_check_disk_usage(self):
        result = self.diagnosis.check_disk_usage()
        self.assertEqual(result, 'Disk usage is within the limit.')

    def test_check_bandwidth_usage(self):
        result = self.diagnosis.check_bandwidth_usage()
        self.assertEqual(result, 'Bandwidth usage is within the limit.')

    def test_check_response_time(self):
        result = self.diagnosis.check_response_time()
        self.assertEqual(result, 'Response time is good.')

    def test_check_client_buffer(self):
        result = self.diagnosis.check_client_buffer()
        self.assertEqual(result, 'Client buffer usage exceeds the limit. You should optimize your Redis configuration '
                                 'or client application.')

    def test_preprocess_input_data(self):
        input_data = {
            'memory_usage': [250, 300, 280, 270, 290],
            'cache_hit_ratio': [0.92, 0.95, 0.89, 0.91, 0.93],
            'connection_count': [1000, 1200, 900, 1100, 1000],
            'slow_query': [1, 2, 3, 4, 5],
            'cpu_usage': [2.5, 3.0, 2.8, 2.7, 2.9],
            'disk_usage': [500, 550, 520, 530, 540],
            'bandwidth_usage': [5, 6, 4, 5, 5],
            'response_time': [5, 6, 7, 8, 9],
            'client_buffer': [1000, 1200, 900, 1000, 1100],
        }
        expected_output = {
            'memory_usage': {'mean': 278, 'max': 300, 'min': 250},
            'cache_hit_ratio': {'mean': 0.92, 'max': 0.95, 'min': 0.89},
            'connection_count': {'mean': 1040, 'max': 1200, 'min': 900},
            'slow_query': {'mean': 3, 'max': 5, 'min': 1},
            'cpu_usage': {'mean': 2.78, 'max': 3.0, 'min': 2.5},
            'disk_usage': {'mean': 528, 'max': 550, 'min': 500},
            'bandwidth_usage': {'mean': 5.0, 'max': 6, 'min': 4},
            'response_time': {'mean': 7.0, 'max': 9, 'min': 5},
            'client_buffer': {'mean': 1040, 'max': 1200, 'min': 900},
        }
        output = preprocess_input_data(input_data)
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
