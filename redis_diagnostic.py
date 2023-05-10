def check_memory_usage(self):
    memory_usage = self.preprocessed_input_data['memory_usage']
    if memory_usage is not None and memory_usage > self.rules['memory_usage']['threshold']['max']:
        return "exceed_limit"
    elif memory_usage is not None and memory_usage < self.rules['memory_usage']['threshold']['min']:
        return "below_limit"
    else:
        return "within_limit"


def check_memory_fragmentation(self):
    memory_fragmentation = self.preprocessed_input_data['memory_fragmentation']
    if memory_fragmentation is not None and memory_fragmentation > self.rules['memory_fragmentation']['threshold'][
        'max']:
        return "exceed_limit"
    elif memory_fragmentation is not None and memory_fragmentation < self.rules['memory_fragmentation']['threshold'][
        'min']:
        return "below_limit"
    else:
        return "within_limit"


def check_cache_hit_rate(self):
    cache_hit_rate = self.preprocessed_input_data['cache_hit_rate']
    if cache_hit_rate is not None and cache_hit_rate < self.rules['cache_hit_rate']['threshold']['min']:
        return "below_limit"
    else:
        return "within_limit"


def check_client_connections(self):
    client_connections = self.preprocessed_input_data['client_connections']
    if client_connections is not None and client_connections > self.rules['client_connections']['threshold']['max']:
        return "exceed_limit"
    elif client_connections is not None and client_connections < self.rules['client_connections']['threshold']['min']:
        return "below_limit"
    else:
        return "within_limit"


def check_evicted_keys(self):
    evicted_keys = self.preprocessed_input_data['evicted_keys']
    if evicted_keys is not None and evicted_keys > self.rules['evicted_keys']['threshold']['max']:
        return "exceed_limit"
    else:
        return "within_limit"


def check_keyspace_hits(self):
    keyspace_hits = self.preprocessed_input_data['keyspace_hits']
    if keyspace_hits is not None and keyspace_hits < self.rules['keyspace_hits']['threshold']['min']:
        return "below_limit"
    else:
        return "within_limit"


def check_keyspace_misses(self):
    keyspace_misses = self.preprocessed_input_data['keyspace_misses']
    if keyspace_misses is not None and keyspace_misses > self.rules['keyspace_misses']['threshold']['max']:
        return "exceed_limit"
    elif keyspace_misses is not None and keyspace_misses < self.rules['keyspace_misses']['threshold']['min']:
        return "below_limit"
    else:
        return "within_limit"


def check_connected_slaves(self):
    connected_slaves = self.preprocessed_input_data['connected_slaves']
    if connected_slaves is not None and connected_slaves < self.rules['connected_slaves']['threshold']['min']:
        return "below_limit"
    else:
        return "within_limit"


def check_blocked_clients(self):
    blocked_clients = self.preprocessed_input_data['blocked_clients']
    max_blocked_clients = self.rules['blocked_clients']['threshold'].get('max')
    min_blocked_clients = self.rules['blocked_clients']['threshold'].get('min')
    if max_blocked_clients is not None and blocked_clients > max_blocked_clients:
        return "exceed_limit"
    elif min_blocked_clients is not None and blocked_clients < min_blocked_clients:
        return "below_limit"
    else:
        return "within_limit"


def check_rejected_connections(self):
    rejected_connections = self.preprocessed_input_data['rejected_connections']
    max_rejected_connections = self.rules['rejected_connections']['threshold'].get('max')
    if max_rejected_connections is not None and rejected_connections > max_rejected_connections:
        return "exceed_limit"
    else:
        return "within_limit"


def check_connected_clients(self):
    connected_clients = self.preprocessed_input_data['connected_clients']
    min_connected_clients = self.rules['connected_clients']['threshold'].get('min')
    if min_connected_clients is not None and connected_clients < min_connected_clients:
        return "below_limit"
    else:
        return "within_limit"


def check_expired_keys(self):
    expired_keys = self.preprocessed_input_data['expired_keys']
    max_expired_keys = self.rules['expired_keys']['threshold'].get('max')
    if max_expired_keys is not None and expired_keys > max_expired_keys:
        return "exceed_limit"
    else:
        return "within_limit"


def check_keyspace_hits(self):
    keyspace_hits = self.preprocessed_input_data['keyspace_hits']
    max_keyspace_hits = self.rules['keyspace_hits']['threshold'].get('max')
    min_keyspace_hits = self.rules['keyspace_hits']['threshold'].get('min')
    if max_keyspace_hits is not None and keyspace_hits > max_keyspace_hits:
        return "exceed_limit"
    elif min_keyspace_hits is not None and keyspace_hits < min_keyspace_hits:
        return "below_limit"
    else:
        return "within_limit"


def check_keyspace_misses(self):
    keyspace_misses = self.preprocessed_input_data['keyspace_misses']
    max_keyspace_misses = self.rules['keyspace_misses']['threshold'].get('max')
    if max_keyspace_misses is not None and keyspace_misses > max_keyspace_misses:
        return "exceed_limit"
    else:
        return "within_limit"


def check_total_connections_received(self):
    total_connections_received = self.preprocessed_input_data['total_connections_received']
    max_total_connections_received = self.rules['total_connections_received']['threshold'].get('max')
    min_total_connections_received = self.rules['total_connections_received']['threshold'].get('min')
    if max_total_connections_received is not None and total_connections_received > max_total_connections_received:
        return "exceed_limit"
    elif min_total_connections_received is not None and total_connections_received < min_total_connections_received:
        return "below_limit"
    else:
        return "within_limit"


def check_instantaneous_ops_per_sec(self):
    instantaneous_ops_per_sec = self.preprocessed_input_data['instantaneous_ops_per_sec']
    max_instantaneous_ops_per_sec = self.rules['instantaneous_ops_per_sec']['threshold'].get('max')
    min_instantaneous_ops_per_sec = self.rules['instantaneous_ops_per_sec']['threshold'].get('min')
    if max_instantaneous_ops_per_sec is not None and instantaneous_ops_per_sec > max_instantaneous_ops_per_sec:
        return "exceed_limit"
    elif min_instantaneous_ops_per_sec is not None and instantaneous_ops_per_sec < min_instantaneous_ops_per_sec:
        return "below_limit"
    else:
        return "within_limit"


def check_instantaneous_input_kbps(self):
    instantaneous_input_kbps = self.preprocessed_input_data['instantaneous_input_kbps']
    max_instantaneous_input_kbps = self.rules['instantaneous_input_kbps']['threshold'].get('max')
    if max_instantaneous_input_kbps is not None and instantaneous_input_kbps > max_instantaneous_input_kbps:
        return "exceed_limit"
    else:
        return "within_limit"


def check_instantaneous_output_kbps(self):
    instantaneous_output_kbps = self.preprocessed_input_data['instantaneous_output_kbps']
    max_instantaneous_output_kbps = self.rules['instantaneous_output_kbps']['threshold'].get('max')
    if max_instantaneous_output_kbps is not None and instantaneous_output_kbps > max_instantaneous_output_kbps:
        return "exceed_limit"
    else:
        return "within_limit"


def check_used_cpu_sys(self):
    used_cpu_sys = self.preprocessed_input_data['used_cpu_sys']
    max_used_cpu_sys = self.rules['used_cpu_sys']['threshold'].get('max')
    if max_used_cpu_sys is not None and used_cpu_sys > max_used_cpu_sys:
        return "exceed_limit"
    else:
        return "within_limit"


def check_used_cpu_user(self):
    used_cpu_user = self.preprocessed_input_data['used_cpu_user']
    max_used_cpu_user = self.rules['used_cpu_user']['threshold'].get('max')
    if max_used_cpu_user is not None and used_cpu_user > max_used_cpu_user:
        return "exceed_limit"
    else:
        return "within_limit"


def check_keys_in_db(self):
    keys_in_db = self.preprocessed_input_data['keys_in_db']
    max_keys_in_db = self.rules['keys_in_db']['threshold'].get('max')
    min_keys_in_db = self.rules['keys_in_db']['threshold'].get('min')
    if max_keys_in_db is not None and keys_in_db > max_keys_in_db:
        return "exceed_limit"
    elif min_keys_in_db is not None and keys_in_db < min_keys_in_db:
        return "below_limit"
    else:
        return "within_limit"
