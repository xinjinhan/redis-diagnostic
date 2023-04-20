import json


class RedisPerformanceDiagnosis:
    def __init__(self, input_data, rules_file_path):
        self.input_data = input_data
        self.rules = self.read_rules_file(rules_file_path)
        self.preprocessed_input_data = self.preprocess_input_data()

    def read_rules_file(self, file_path):
        # 从 JSON 文件中读取诊断规则和对应参数
        with open(file_path, 'r') as f:
            rules = json.load(f)
        return rules

    def preprocess_input_data(self):
        # 对输入数据进行预处理，包括计算平均值、最大值和最小值
        preprocessed_input_data = {}
        for metric, data in self.input_data.items():
            mean = round(sum(data) / len(data),2)
            maximum = max(data)
            minimum = min(data)
            preprocessed_input_data[metric] = {'mean': mean, 'max': maximum, 'min': minimum}
        return preprocessed_input_data

    def check_memory_usage(self):
        # 检查内存使用率是否超出限制
        memory_usage = self.preprocessed_input_data['memory_usage']
        mean_memory_usage = memory_usage['mean']
        max_memory_usage = self.rules['memory_usage']['threshold']['max']
        min_memory_usage = self.rules['memory_usage']['threshold']['min']
        if mean_memory_usage / max_memory_usage >= 1:
            return self.rules['memory_usage']['exceed_limit']
        elif memory_usage['min'] / min_memory_usage <= 1:
            return self.rules['memory_usage']['too_low']
        else:
            return self.rules['memory_usage']['within_limit']

    def check_cache_hit_ratio(self):
        # 检查缓存命中率是否低于阈值
        cache_hit_ratio = self.preprocessed_input_data['cache_hit_ratio']
        mean_cache_hit_ratio = cache_hit_ratio['mean']
        min_cache_hit_ratio = self.rules['cache_hit_ratio']['threshold']['min']
        if mean_cache_hit_ratio < min_cache_hit_ratio:
            if mean_cache_hit_ratio < 0.2:
                return self.rules['cache_hit_ratio']['very_low']
            else:
                return self.rules['cache_hit_ratio']['too_low']
        else:
            return self.rules['cache_hit_ratio']['good']

    def check_connection_count(self):
        # 检查连接数是否超出限制
        connection_count = self.preprocessed_input_data['connection_count']
        mean_connection_count = connection_count['mean']
        max_connection_count = self.rules['connection_count']['threshold']['max']
        min_connection_count = self.rules['connection_count']['threshold']['min']
        if mean_connection_count / max_connection_count >= 1:
            return self.rules['connection_count']['exceed_limit']
        elif mean_connection_count < min_connection_count:
            return self.rules['connection_count']['too_low']
        elif connection_count['max'] / max_connection_count >= 1:
            return self.rules['connection_count']['exceed_limit']
        else:
            return self.rules['connection_count']['within_limit']

    def check_slow_query(self):
        # 检查慢查询数是否超出限制
        slow_query_count = self.preprocessed_input_data['slow_query']
        mean_slow_query_count = slow_query_count['mean']
        max_slow_query_count = self.rules['slow_query']['threshold']['max']
        if mean_slow_query_count / max_slow_query_count >= 1:
            return self.rules['slow_query']['exceed_limit']
        else:
            return self.rules['slow_query']['within_limit']

    def check_cpu_usage(self):
        # 检查 CPU 使用率是否超出限制
        cpu_usage = self.preprocessed_input_data['cpu_usage']
        mean_cpu_usage = cpu_usage['mean']
        max_cpu_usage = self.rules['cpu_usage']['threshold']['max']
        if mean_cpu_usage / max_cpu_usage >= 1:
            return self.rules['cpu_usage']['exceed_limit']
        else:
            return self.rules['cpu_usage']['within_limit']

    def diagnose(self):
        # 对所有指标进行诊断，并返回诊断结果和优化建议
        results = {}
        results['memory_usage'] = self.check_memory_usage()
        results['cache_hit_ratio'] = self.check_cache_hit_ratio()
        results['connection_count'] = self.check_connection_count()
        results['slow_query'] = self.check_slow_query()
        results['cpu_usage'] = self.check_cpu_usage()
        return results
