Spanning tree is configured on SWITCH

- global config level
spanning-tree vlan 1 root primary
spanning-tree portfast default
spanning-tree portfast bpduguard default
errdisable recovery cause bpduguard
errdisable recovery interval 30 :(

- interface config level
spanning-tree portfast enable
spanning-tree portfast trunk
spanning-tree bpduguard enable
spanning-tree guard root
