#!/bin/bash

echo "Building charm-designate-bind with new interface......."

cd designate-bind/
tox -e build
cd ..

mkdir designate-bind/build/builds/designate-bind/hooks/relations/neutron-recursive-dns/
cp -r interface-neutron-recursive-dns/* designate-bind/build/builds/designate-bind/hooks/relations/neutron-recursive-dns/

cp designate-bind/build/builds/designate-bind/hooks/dns-backend-relation-changed designate-bind/build/builds/designate-bind/hooks/neutron-recursive-dns-broken
cp designate-bind/build/builds/designate-bind/hooks/dns-backend-relation-changed designate-bind/build/builds/designate-bind/hooks/neutron-recursive-dns-joined
cp designate-bind/build/builds/designate-bind/hooks/dns-backend-relation-changed designate-bind/build/builds/designate-bind/hooks/neutron-recursive-dns-departed
cp designate-bind/build/builds/designate-bind/hooks/dns-backend-relation-changed designate-bind/build/builds/designate-bind/hooks/neutron-recursive-dns-changed


echo "charm-designate-bind built"

echo "Building neutron-gateway with new hook......"

cp neutron-gateway/hooks/neutron_hooks.py neutron-gateway/hooks/neutron-recursive-dns-relation-broken
cp neutron-gateway/hooks/neutron_hooks.py neutron-gateway/hooks/neutron-recursive-dns-relation-joined
cp neutron-gateway/hooks/neutron_hooks.py neutron-gateway/hooks/neutron-recursive-dns-relation-changed
cp neutron-gateway/hooks/neutron_hooks.py neutron-gateway/hooks/neutron-recursive-dns-relation-departed

echo "neutron-gateway built"
