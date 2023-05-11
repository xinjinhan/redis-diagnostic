class RedisDiagnosticTool:
    def __init__(self, preprocessed_input_data, rules):
        self.preprocessed_input_data = preprocessed_input_data
        self.rules = rules

    def check_memory_usage_ratio(self):
        memory_usage_ratio = self.preprocessed_input_data['memory_usage_ratio']
        if memory_usage_ratio:
            mean_memory_usage_ratio = memory_usage_ratio['mean']
            max_memory_usage_ratio = self.rules['memory_usage_ratio']['threshold']['max']
            min_memory_usage_ratio = self.rules['memory_usage_ratio']['threshold']['min']
            if mean_memory_usage_ratio > max_memory_usage_ratio:
                return "exceed_limit"
            elif mean_memory_usage_ratio < min_memory_usage_ratio:
                return "too_low"
            else:
                return "within_limit"
        else:
            return "unknown"

    def check_memory_fragmentation(self):
        memory_fragmentation = self.preprocessed_input_data['memory_fragmentation']
        if memory_fragmentation:
            mean_memory_fragmentation = memory_fragmentation['mean']
            max_memory_fragmentation = self.rules['memory_fragmentation']['threshold']['max']
            if mean_memory_fragmentation > max_memory_fragmentation:
                return "exceed_limit"
            else:
                return "within_limit"
        else:
            return "unknown"

    def check_cache_hit_rate(self):
        cache_hit_rate = self.preprocessed_input_data['cache_hit_rate']
        if cache_hit_rate:
            mean_cache_hit_rate = cache_hit_rate['mean']
            min_cache_hit_rate = self.rules['cache_hit_rate']['threshold']['min']
            if mean_cache_hit_rate < min_cache_hit_rate:
                return "below_limit"
            else:
                return "within_limit"
        else:
            return "unknown"

    def check_client_connections(self):
        client_connections = self.preprocessed_input_data['client_connections']
        if client_connections:
            mean_client_connections = client_connections['mean']
            max_client_connections = self.rules['client_connections']['threshold']['max']
            if mean_client_connections > max_client_connections:
                return "exceed_limit"
            else:
                return "within_limit"
        else:
            return "unknown"

    def check_slow_queries(self):
        slow_queries = self.preprocessed_input_data['slow_queries']
        if slow_queries:
            mean_slow_queries = slow_queries['mean']
            max_slow_queries = self.rules['slow_queries']['threshold']['max']
            if mean_slow_queries > max_slow_queries:
                return "exceed_limit"
            else:
                return "within_limit"
        else:
            return "unknown"

    def check_network_latency(self):
        network_latency = self.preprocessed_input_data['network_latency']
        if network_latency:
            mean_network_latency = network_latency['mean']
            max_network_latency = self.rules['network_latency']['threshold']['max']
            if mean_network_latency > max_network_latency:
                return "exceed_limit"
            else:
                return "within_limit"
        else:
            return "unknown"

    def check_master_slave_sync_latency(self):
        master_slave_sync_latency = self.preprocessed_input_data['master_slave_sync_latency']
        if master_slave_sync_latency:
            mean_master_slave_sync_latency = master_slave_sync_latency['mean']
            max_master_slave_sync_latency = self.rules['master_slave_sync_latency']['threshold']['max']
            if mean_master_slave_sync_latency > max_master_slave_sync_latency:
                return "exceed_limit"
            else:
                return "within_limit"
        else:
            return "unknown"

    def check_aof_rdb_duration(self):
        aof_rdb_duration = self.preprocessed_input_data['aof_rdb_duration']
        if aof_rdb_duration:
            mean_aof_rdb_duration = aof_rdb_duration['mean']
            max_aof_rdb_duration = self.rules['aof_rdb_duration']['threshold']['max']
            if mean_aof_rdb_duration > max_aof_rdb_duration:
                return "exceed_limit"
            else:
                return "within_limit"
        else:
            return "unknown"

    def check_evicted_keys(self):
        evicted_keys = self.preprocessed_input_data['evicted_keys']
        if evicted_keys:
            mean_evicted_keys = evicted_keys['mean']
            max_evicted_keys = self.rules['evicted_keys']['threshold']['max']
            if mean_evicted_keys > max_evicted_keys:
                return "exceed_limit"
            else:
                return "within_limit"
        else:
            return "unknown"

    def check_expired_keys(self):
        expired_keys = self.preprocessed_input_data['expired_keys']
        if expired_keys:
            mean_expired_keys = expired_keys['mean']
            max_expired_keys = self.rules['expired_keys']['threshold']['max']
            if mean_expired_keys > max_expired_keys:
                return "exceed_limit"
            else:
                return "within_limit"
        else:
            return "unknown"

    def check_keyspace_hits(self):
        keyspace_hits = self.preprocessed_input_data['keyspace_hits']
        if keyspace_hits:
            mean_keyspace_hits = keyspace_hits['mean']
            max_keyspace_hits = self.rules['keyspace_hits']['threshold']['max']
            min_keyspace_hits = self.rules['keyspace_hits']['threshold']['min']
            if mean_keyspace_hits > max_keyspace_hits:
                return "exceed_limit"
            elif mean_keyspace_hits < min_keyspace_hits:
                return "too_low"
            else:
                return "within_limit"
        else:
            return "unknown"

    def check_keyspace_misses(self):
        keyspace_misses = self.preprocessed_input_data['keyspace_misses']
        if keyspace_misses:
            mean_keyspace_misses = keyspace_misses['mean']
            max_keyspace_misses = self.rules['keyspace_misses']['threshold']['max']
            if mean_keyspace_misses > max_keyspace_misses:
                return "exceed_limit"
            else:
                return "within_limit"
        else:
            return "unknown"

    def check_blocked_clients(self):
        blocked_clients = self.preprocessed_input_data['blocked_clients']
        if blocked_clients:
            mean_blocked_clients = blocked_clients['mean']
            max_blocked_clients = self.rules['blocked_clients']['threshold']['max']
            if mean_blocked_clients > max_blocked_clients:
                return "exceed_limit"
            else:
                return "within_limit"
        else:
            return "unknown"

    def check_total_connections_received(self):
        total_connections_received = self.preprocessed_input_data['total_connections_received']
        if total_connections_received:
            mean_total_connections_received = total_connections_received['mean']
            max_total_connections_received = self.rules['total_connections_received']['threshold']['max']
            min_total_connections_received = self.rules['total_connections_received']['threshold']['min']
            if mean_total_connections_received > max_total_connections_received:
                return "exceed_limit"
            elif mean_total_connections_received < min_total_connections_received:
                return "too_low"
            else:
                return "within_limit"
        else:
            return "unknown"

    def check_instantaneous_ops_per_sec(self):
        instantaneous_ops_per_sec = self.preprocessed_input_data['instantaneous_ops_per_sec']
        if instantaneous_ops_per_sec:
            mean_instantaneous_ops_per_sec = instantaneous_ops_per_sec['mean']
            max_instantaneous_ops_per_sec = self.rules['instantaneous_ops_per_sec']['threshold']['max']
            min_instantaneous_ops_per_sec = self.rules['instantaneous_ops_per_sec']['threshold']['min']
            if mean_instantaneous_ops_per_sec > max_instantaneous_ops_per_sec:
                return "exceed_limit"
            elif mean_instantaneous_ops_per_sec < min_instantaneous_ops_per_sec:
                return "too_low"
            else:
                return "within_limit"
        else:
            return "unknown"

    def check_instantaneous_input_kbps(self):
        instantaneous_input_kbps = self.preprocessed_input_data['instantaneous_input_kbps']
        if instantaneous_input_kbps:
            mean_instantaneous_input_kbps = instantaneous_input_kbps['mean']
            max_instantaneous_input_kbps = self.rules['instantaneous_input_kbps']['threshold']['max']
            if mean_instantaneous_input_kbps > max_instantaneous_input_kbps:
                return "exceed_limit"
            else:
                return "within_limit"
        else:
            return "unknown"

    def check_instantaneous_output_kbps(self):
        instantaneous_output_kbps = self.preprocessed_input_data['instantaneous_output_kbps']
        if instantaneous_output_kbps:
            mean_instantaneous_output_kbps = instantaneous_output_kbps['mean']
            max_instantaneous_output_kbps = self.rules['instantaneous_output_kbps']['threshold']['max']
            if mean_instantaneous_output_kbps > max_instantaneous_output_kbps:
                return "exceed_limit"
            else:
                return "within_limit"
        else:
            return "unknown"

    def check_used_cpu_sys(self):
        used_cpu_sys = self.preprocessed_input_data['used_cpu_sys']
        if used_cpu_sys:
            mean_used_cpu_sys = used_cpu_sys['mean']
            max_used_cpu_sys = self.rules['used_cpu_sys']['threshold']['max']
            if mean_used_cpu_sys > max_used_cpu_sys:
                return "exceed_limit"
            else:
                return "within_limit"
        else:
            return "unknown"

    def check_used_cpu_user(self):
        used_cpu_user = self.preprocessed_input_data['used_cpu_user']
        if used_cpu_user:
            mean_used_cpu_user = used_cpu_user['mean']
            max_used_cpu_user = self.rules['used_cpu_user']['threshold']['max']
            if mean_used_cpu_user > max_used_cpu_user:
                return "exceed_limit"
            else:
                return "within_limit"
        else:
            return "unknown"

    def check_keys_in_db(self):
        keys_in_db = self.preprocessed_input_data['keys_in_db']
        if keys_in_db:
            mean_keys_in_db = keys_in_db['mean']
            min_keys_in_db = self.rules['keys_in_db']['threshold']['min']
            max_keys_in_db = self.rules['keys_in_db']['threshold']['max']
            if mean_keys_in_db < min_keys_in_db:
                return "too_low"
            elif mean_keys_in_db > max_keys_in_db:
                return "exceed_limit"
            else:
                return "within_limit"
        else:
            return "unknown"

    def check_used_memory_rss(self):
        used_memory_rss = self.preprocessed_input_data['used_memory_rss']
        if used_memory_rss:
            mean_used_memory_rss = used_memory_rss['mean']
            max_used_memory_rss = self.rules['used_memory_rss']['threshold']['max']
            if mean_used_memory_rss > max_used_memory_rss:
                return "exceed_limit"
            else:
                return "within_limit"
        else:
            return "unknown"

