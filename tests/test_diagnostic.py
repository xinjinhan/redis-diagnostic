import unittest
from redis_diagnostic import RedisPerformanceDiagnosis

class TestRedisPerformanceDiagnosis(unittest.TestCase):
    def setUp(self):
        input_data = {
            'memory_usage': 250,
            'cache_hit_ratio': 0.92,
            'connection_count': 1000,
            'slow_query': [1, 2, 3, 4, 5],
            'cpu_usage': 2.5,
            'disk_usage': 0.5,
            'bandwidth_usage': 5,
            'response_time': [5, 6, 7, 8, 9],
            'client_buffer': 1000,
            'max_memory': 500,
            'max_clients': 2000,
            'slowlog_max_len': 10,
            'server_cpu_cores': 4,
            'max_bandwidth': 10,
            'client_buffer_peak_usage': 2000,
        }
        self.diagnosis = RedisPerformanceDiagnosis(**input_data)

    def test_check_memory_usage_within_limit(self):
        self.assertEqual(self.diagnosis.check_memory_usage(), 'Memory usage is within the limit.')

    def test_check_memory_usage_exceeds_limit(self):
        self.diagnosis.memory_usage = 600
        self.assertEqual(self.diagnosis.check_memory_usage(), 'Memory usage exceeds the limit. You should increase the memory limit.')

    def test_check_cache_hit_ratio_good(self):
        self.assertEqual(self.diagnosis.check_cache_hit_ratio(), 'Cache hit ratio is good.')

    def test_check_cache_hit_ratio_low(self):
        self.diagnosis.cache_hit_ratio = 0.8
        self.assertEqual(self.diagnosis.check_cache_hit_ratio(), 'Cache hit ratio is low. You should check your caching strategy.')

    def test_check_connection_count_within_limit(self):
        self.assertEqual(self.diagnosis.check_connection_count(), 'Connection count is within the limit.')

    def test_check_connection_count_exceeds_limit(self):
        self.diagnosis.connection_count = 3000
        self.assertEqual(self.diagnosis.check_connection_count(), 'Connection count exceeds the limit. You should increase the max clients limit.')

    def test_check_slow_query_within_limit(self):
        self.assertEqual(self.diagnosis.check_slow_query(), 'Slow query count is within the limit.')

    def test_check_slow_query_exceeds_limit(self):
        self.diagnosis.slow_query = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.assertEqual(self.diagnosis.check_slow_query(), 'There are too many slow queries. You should optimize your queries or increase the slowlog max len.')

    def test_check_cpu_usage_within_limit(self):
        self.assertEqual(self.diagnosis.check_cpu_usage(), 'CPU usage is within the limit.')

    def test_check_cpu_usage_exceeds_limit(self):
        self.diagnosis.cpu_usage = 10
        self.assertEqual(self.diagnosis.check_cpu_usage(), 'CPU usage exceeds the limit. You should optimize your Redis configuration or upgrade your server.')

    def test_check_disk_usage_within_limit(self):
        self.assertEqual(self.diagnosis.check_disk_usage(), 'Disk usage is within the limit.')

    def test_check_disk_usage_exceeds_limit(self):
        self.diagnosis.disk_usage = 1000
        self.assertEqual(self.diagnosis.check_disk_usage(), 'Disk usage exceeds the limit. You should increase the memory limit or clean up the disk.')

    def test_check_bandwidth_usage_within_limit(self):
        self.assertEqual(self.diagnosis.check_bandwidth_usage(), 'Bandwidth usage is within the limit.')

    def test_check_bandwidth_usage_exceeds_limit(self):
        self.diagnosis.bandwidth_usage = 20
        self.assertEqual(self.diagnosis.check_bandwidth_usage(), 'Bandwidth usage exceeds the limit. You should check your network connection.')

    def test_check_response_time_good(self):
        self.assertEqual(self.diagnosis.check_response_time(), 'Response time is good.')

    def test_check_response_time_slow(self):
        self.diagnosis.response_time = [5, 6, 7, 8, 10]
        self.assertEqual(self.diagnosis.check_response_time(), 'Response time is slow. You should optimize your Redis configuration or network connection.')

    def test_check_client_buffer_within_limit(self):
        self.assertEqual(self.diagnosis.check_client_buffer(), 'Client buffer usage is within the limit.')

    def test_check_client_buffer_exceeds_limit(self):
        self.diagnosis.client_buffer = 3000
        self.assertEqual(self.diagnosis.check_client_buffer(), 'Client buffer usage exceeds the limit. You should optimize your Redis configuration or client application.')

if __name__ == '__main__':
    unittest.main()
