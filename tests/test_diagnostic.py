import json
import unittest
from redis_diagnostic import RedisPerformanceDiagnosis


class TestRedisPerformanceDiagnosis(unittest.TestCase):
    def setUp(self):
        self.rules_file_path = 'redis_performance_rules.json'
        self.input_data = {
            'memory_usage': [100, 120, 140, 160, 180],
            'cache_hit_ratio': [0.85, 0.87, 0.88, 0.9, 0.91],
            'connection_count': [100, 110, 120, 130, 140],
            'slow_query': [10, 8, 12, 15, 20],
            'cpu_usage': [0.7, 0.8, 0.9, 0.85, 0.95]
        }

    def test_check_memory_usage(self):
        # 测试内存使用率是否在限制范围内
        diagnosis = RedisPerformanceDiagnosis(self.input_data, self.rules_file_path)
        result = diagnosis.check_memory_usage()
        expected = diagnosis.rules['memory_usage']['within_limit']
        self.assertEqual(result, expected)
        # 测试内存使用率是否超出最大值
        diagnosis = RedisPerformanceDiagnosis(self.input_data, self.rules_file_path)
        diagnosis.rules['memory_usage']['threshold']['max'] = 130
        result = diagnosis.check_memory_usage()
        expected = diagnosis.rules['memory_usage']['exceed_limit']
        self.assertEqual(result, expected)
        # 测试内存使用率是否低于最小值
        diagnosis = RedisPerformanceDiagnosis(self.input_data, self.rules_file_path)
        diagnosis.rules['memory_usage']['threshold']['max'] = 1024
        diagnosis.rules['memory_usage']['threshold']['min'] = 200
        result = diagnosis.check_memory_usage()
        expected = diagnosis.rules['memory_usage']['too_low']
        self.assertEqual(result, expected)

    def test_check_cache_hit_ratio(self):
        # 测试缓存命中率是否良好
        diagnosis = RedisPerformanceDiagnosis(self.input_data, self.rules_file_path)
        result = diagnosis.check_cache_hit_ratio()
        expected = diagnosis.rules['cache_hit_ratio']['good']
        self.assertEqual(result, expected)
        # 测试缓存命中率是否太低
        diagnosis = RedisPerformanceDiagnosis(self.input_data, self.rules_file_path)
        diagnosis.preprocessed_input_data['cache_hit_ratio']['mean'] = 0.3
        result = diagnosis.check_cache_hit_ratio()
        expected = diagnosis.rules['cache_hit_ratio']['too_low']
        self.assertEqual(result, expected)
        # 测试缓存命中率是否非常低
        diagnosis = RedisPerformanceDiagnosis(self.input_data, self.rules_file_path)
        diagnosis.preprocessed_input_data['cache_hit_ratio']['mean'] = 0.1
        result = diagnosis.check_cache_hit_ratio()
        expected = diagnosis.rules['cache_hit_ratio']['very_low']
        self.assertEqual(result, expected)

    def test_check_connection_count(self):
        # 测试连接数是否在限制范围内
        diagnosis = RedisPerformanceDiagnosis(self.input_data, self.rules_file_path)
        result = diagnosis.check_connection_count()
        expected = diagnosis.rules['connection_count']['within_limit']
        self.assertEqual(result, expected)
        # 测试连接数是否超出最大值
        diagnosis = RedisPerformanceDiagnosis(self.input_data, self.rules_file_path)
        diagnosis.rules['connection_count']['threshold']['max'] = 120
        result = diagnosis.check_connection_count()
        expected = diagnosis.rules['connection_count']['exceed_limit']
        self.assertEqual(result, expected)
        # 测试连接数是否太低
        diagnosis = RedisPerformanceDiagnosis(self.input_data, self.rules_file_path)
        diagnosis.rules['connection_count']['threshold']['min'] = 130
        result = diagnosis.check_connection_count()
        expected = diagnosis.rules['connection_count']['too_low']
        self.assertEqual(result, expected)

    def test_check_slow_query(self):
        diagnosis = RedisPerformanceDiagnosis(self.input_data, self.rules_file_path)
        # 测试慢查询是否在限制范围内
        result = diagnosis.check_slow_query()
        expected = diagnosis.rules['slow_query']['within_limit']
        self.assertEqual(result, expected)
        # 测试慢查询是否超出最大值
        diagnosis.rules['slow_query']['threshold']['max'] = 10
        result = diagnosis.check_slow_query()
        expected = diagnosis.rules['slow_query']['exceed_limit']
        self.assertEqual(result, expected)

    def test_check_cpu_usage(self):
        # 测试 CPU 使用率是否在限制范围内
        diagnosis = RedisPerformanceDiagnosis(self.input_data, self.rules_file_path)
        result = diagnosis.check_cpu_usage()
        expected = diagnosis.rules['cpu_usage']['within_limit']
        self.assertEqual(result, expected)
        # 测试 CPU 使用率是否超出最大值
        diagnosis = RedisPerformanceDiagnosis(self.input_data, self.rules_file_path)
        diagnosis.rules['cpu_usage']['threshold']['max'] = 0.8
        result = diagnosis.check_cpu_usage()
        expected = diagnosis.rules['cpu_usage']['exceed_limit']
        self.assertEqual(result, expected)

    def test_diagnose(self):
        # 测试诊断结果是否包含所有问题
        diagnosis = RedisPerformanceDiagnosis(self.input_data, self.rules_file_path)
        result = diagnosis.diagnose()
        expected = {
            'memory_usage': diagnosis.rules['memory_usage']['within_limit'],
            'cache_hit_ratio': diagnosis.rules['cache_hit_ratio']['good'],
            'connection_count': diagnosis.rules['connection_count']['within_limit'],
            'slow_query': diagnosis.rules['slow_query']['within_limit'],
            'cpu_usage': diagnosis.rules['cpu_usage']['within_limit']
        }
        self.assertEqual(result, expected)

        # 修改内存使用率阈值，测试内存使用率是否超过限制
        diagnosis = RedisPerformanceDiagnosis(self.input_data, self.rules_file_path)
        diagnosis.rules['memory_usage']['threshold']['max'] = 120
        result = diagnosis.diagnose()
        expected = {
            'memory_usage': diagnosis.rules['memory_usage']['exceed_limit'],
            'cache_hit_ratio': diagnosis.rules['cache_hit_ratio']['good'],
            'connection_count': diagnosis.rules['connection_count']['within_limit'],
            'slow_query': diagnosis.rules['slow_query']['within_limit'],
            'cpu_usage': diagnosis.rules['cpu_usage']['within_limit']
        }
        result_str = str(result)
        expected_str = str(expected)
        self.assertEqual(result_str, expected_str)

        # 修改 CPU 使用率阈值，测试 CPU 使用率是否超过限制
        diagnosis = RedisPerformanceDiagnosis(self.input_data, self.rules_file_path)
        diagnosis.rules['cpu_usage']['threshold']['max'] = 0.8
        result = diagnosis.diagnose()
        expected = {
            'memory_usage': diagnosis.rules['memory_usage']['within_limit'],
            'cache_hit_ratio': diagnosis.rules['cache_hit_ratio']['good'],
            'connection_count': diagnosis.rules['connection_count']['within_limit'],
            'slow_query': diagnosis.rules['slow_query']['within_limit'],
            'cpu_usage': diagnosis.rules['cpu_usage']['exceed_limit']
        }
        result_str = str(result)
        expected_str = str(expected)
        self.assertEqual(result_str, expected_str)

    def test_preprocess_data(self):
        data = {
            "memory_usage": [100, 200, 300],
            "cache_hit_ratio": [0.8, 0.7, 0.6],
            "connection_count": [500, 400, 300],
            "slow_query": [5, 10, 15],
            "cpu_usage": [0.5, 0.6, 0.7],
            "disk_usage": [0.7, 0.8, 0.9],
            "bandwidth_usage": [50, 60, 70],
            "response_time": [0.02, 0.03, 0.04],
            "client_buffer": [1024, 2048, 3072]
        }
        diagnosis = RedisPerformanceDiagnosis(data, self.rules_file_path)
        p_data = diagnosis.preprocess_input_data()

        # Test if the length of the preprocessed data is correct
        self.assertEqual(len(p_data), len(data))

        # Test if the average, minimum and maximum values are correctly calculated for each metric
        self.assertEqual(p_data['memory_usage']['mean'], 200)
        self.assertEqual(p_data['memory_usage']['min'], 100)
        self.assertEqual(p_data['memory_usage']['max'], 300)

        self.assertEqual(p_data['cache_hit_ratio']['mean'], 0.7)
        self.assertEqual(p_data['cache_hit_ratio']['min'], 0.6)
        self.assertEqual(p_data['cache_hit_ratio']['max'], 0.8)

        self.assertEqual(p_data['connection_count']['mean'], 400)
        self.assertEqual(p_data['connection_count']['min'], 300)
        self.assertEqual(p_data['connection_count']['max'], 500)

        self.assertEqual(p_data['slow_query']['mean'], 10)
        self.assertEqual(p_data['slow_query']['min'], 5)
        self.assertEqual(p_data['slow_query']['max'], 15)

        self.assertEqual(p_data['cpu_usage']['mean'], 0.6)
        self.assertEqual(p_data['cpu_usage']['min'], 0.5)
        self.assertEqual(p_data['cpu_usage']['max'], 0.7)

        self.assertEqual(p_data['disk_usage']['mean'], 0.8)
        self.assertEqual(p_data['disk_usage']['min'], 0.7)
        self.assertEqual(p_data['disk_usage']['max'], 0.9)

        self.assertEqual(p_data['bandwidth_usage']['mean'], 60)
        self.assertEqual(p_data['bandwidth_usage']['min'], 50)
        self.assertEqual(p_data['bandwidth_usage']['max'], 70)

        self.assertEqual(p_data['response_time']['mean'], 0.03)
        self.assertEqual(p_data['response_time']['min'], 0.02)
        self.assertEqual(p_data['response_time']['max'], 0.04)

        self.assertEqual(p_data['client_buffer']['mean'], 2048)
        self.assertEqual(p_data['client_buffer']['min'], 1024)
        self.assertEqual(p_data['client_buffer']['max'], 3072)
