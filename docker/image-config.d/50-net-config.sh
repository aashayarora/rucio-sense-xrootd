#!/bin/bash

# Fix IPv6 Routing
current_gateway=$(ip -6 route show default | awk '/default/{print $3}')
new_gateway=$NET_GATEWAY

if [ "$current_gateway" == "$new_gateway" ]; then
  continue
else
  ip -6 route delete default
  ip -6 route add default via "$new_gateway"
fi