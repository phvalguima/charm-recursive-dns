#!/usr/bin/python
#
# Copyright 2016 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from charms.reactive import RelationBase
from charms.reactive import hook
from charms.reactive import scopes
from charms.reactive.bus import get_states

from charmhelpers.core import hookenv
from charmhelpers.contrib.network import ip as ch_ip


class NeutronRecursiveDNSProvides(RelationBase):
    scope = scopes.GLOBAL

    @hook('{provides:neutron-recursive-dns}-relation-joined')
    def joined(self):
        conv = self.conversation()
        conv.set_state('{relation_name}.related')
        #conv.set_remote('recursive-dns-address',
        #                ch_ip.get_relation_ip(conv.relation_name))
        for relid in hookenv.relation_ids('neutron-recursive-dns'):
            hookenv.log("NeutronRecursiveDNSProvides relid: {}".format(relid))
            hookenv.relation_set(relation_id=relid,recursive_ip=ch_ip.get_relation_ip(conv.relation_name))

    @hook('{provides:neutron-recursive-dns}-relation-departed')
    def departed(self):
        conv = self.conversation()
        conv.remove_state('{relation_name}.related')