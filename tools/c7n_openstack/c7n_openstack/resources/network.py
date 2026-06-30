# Copyright The Cloud Custodian Authors.
# SPDX-License-Identifier: Apache-2.0
#
from c7n_openstack.query import QueryResourceManager, TypeInfo
from c7n_openstack.provider import resources


@resources.register('network')
class Network(QueryResourceManager):
    class resource_type(TypeInfo):
        enum_spec = ('list_networks', None)
        id = 'id'
        name = 'name'
        default_report_fields = ['id', 'name', 'status', 'shared']

    def resources(self, query=None):
        q = query or self.get_resource_query()
        key = self.get_cache_key(q)
        resources = [r.toDict() for r in self.augment(self.source.get_resources(q))]
        self._cache.save(key, resources)
        return self.filter_resources(resources)


@resources.register('subnet')
class Subnet(QueryResourceManager):
    class resource_type(TypeInfo):
        enum_spec = ('list_subnets', None)
        id = 'id'
        name = 'name'
        default_report_fields = ['id', 'name', 'cidr', 'network_id']

    def resources(self, query=None):
        q = query or self.get_resource_query()
        key = self.get_cache_key(q)
        resources = [r.toDict() for r in self.augment(self.source.get_resources(q))]
        self._cache.save(key, resources)
        return self.filter_resources(resources)


@resources.register('router')
class Router(QueryResourceManager):
    class resource_type(TypeInfo):
        enum_spec = ('list_routers', None)
        id = 'id'
        name = 'name'
        default_report_fields = ['id', 'name', 'status', 'external_gateway_info']

    def resources(self, query=None):
        q = query or self.get_resource_query()
        key = self.get_cache_key(q)
        resources = [r.toDict() for r in self.augment(self.source.get_resources(q))]
        self._cache.save(key, resources)
        return self.filter_resources(resources)


@resources.register('floating-ip')
class FloatingIP(QueryResourceManager):
    class resource_type(TypeInfo):
        enum_spec = ('list_floating_ips', None)
        id = 'id'
        name = 'floating_ip_address'
        default_report_fields = ['id', 'floating_ip_address', 'status', 'port_id']

    def resources(self, query=None):
        q = query or self.get_resource_query()
        key = self.get_cache_key(q)
        resources = [r.toDict() for r in self.augment(self.source.get_resources(q))]
        self._cache.save(key, resources)
        return self.filter_resources(resources)
