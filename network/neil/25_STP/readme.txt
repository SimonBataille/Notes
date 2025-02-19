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

---

Layer 3 Path Selection and Loop Prevention Review
- Layer 3 routing and HSRP control the path selection and provide automatic failover for Layer 3 connections
- Dynamic routing protocols have built-in loop prevention mechanisms and TTL acts as a final failsafe
- How will path selection, failover and loop prevention work for the Layer 2 only switches?

Why we have the Spanning Tree Protocol
- The Layer 2 Ethernet header does not have a TTL field to stop the looping traffic
- The Spanning Tree Protocol is used to prevent Layer 2 loops : It does this by detecting potential loops and blocking ports to prevent them
- The access layer switches can only use half of their physically cabled uplink bandwidth : Spanning Tree is a necessary evil because a broadcast storm would be a far worse scenario

STP Terminology – The Bridge
- Spanning Tree was invented back when bridges were in use so it uses that terminology (the ‘Root Bridge’ and ‘Bridge Protocol Data Units’)

How Spanning Tree Works
- Spanning Tree is an industry standard protocol and is enabled by default on all vendor’s switches
- Switches send Bridge Protocol Data Units out all ports when they come online. These are used to detect other switches and potential loops
- The switch will not forward traffic out any port until it is certain it is loop free : If there is no loop the port will transition to Forwarding

- The BPDU contains the switch’s Bridge ID which uniquely identifies the switch on the LAN
- The Bridge ID is comprised of the switch’s unique MAC address and an administrator defined Bridge Priority value (0 – 65535, 32768 default)

- Root Bridge : The switch with the lowest Bridge Priority value is preferred (16384 is better than 49152),In the case of a tie the switch with the lowest MAC address will be selected
- The other switches will detect their lowest cost path to the Root Bridge

- Spanning Tree Cost : Short-Mode (default, 16 bits) vs Long-Mode(32 bits)
- Acc4#show spanning-tree pathcost method
- SW1(config)# spanning-tree pathcost method long
