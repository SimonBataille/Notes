Why we have EtherChannel
- Oversubscription : 20:1 from the access to the distribution layer, 4:1 for the distribution to core layer links
- A Spanning Tree instance provides redundancy, but not load balancing
- If a switch has multiple equal cost paths via the same neighbour switch towards the Root Bridge, it will select the port with the lowest Port ID
- Etherchannel groups multiple physical interfaces into a single logical interface
- Traffic is load balanced across all the links in the EtherChannel

EtherChannel Load Balancing
- A single flow is load balanced onto a single port channel interface
- Any single flow receives the bandwidth of a single link in the port channel as a maximum
- You can think of a port channel as a multi-lane motorway. The cars stay in a single lane, but because there are multiple lanes the overall traffic gets there quicker 

EtherChannel Protocols and Configuration
- Link Aggregation Control Protocol, Port Aggregation Protocol, Static Etherchannel
- The switches on both sides must have a matching configuration : Speed and duplex, Access or Trunk mode, Native VLAN and allowed VLANs on trunks, Access VLAN on access ports

- LACP interfaces can be set as either Active or Passive
- PAgP interfaces can be set as either Desirable or Auto
- SW1(config)#interface range f0/23 - 24
- SW1(config-if-range)#channel-group 1 mode active/desirable/on : This creates interface port-channel 1
- SW1(config)#interface port-channel 1 : Configure the interface settings on the port channe
- SW1(config-if)#switchport mode trunk

- show etherchannel summary
- show spannin-tree vlan 1

StackWise, VSS and vPC : Multi-Chassis technologies
- EtherChannel across Redundant Switches : Spanning Tree will see the port channels as two separate interfaces and block one path if a loop is formed
- Cisco support Multi-chassis EtherChannel technologies on some switches
- These switches support a shared EtherChannel from different switches : Spanning Tree is still enabled but it does not detect any loops
- StackWise/VSS Virtual Switching System (Catalyst switch), vPC Virtual Port Channel (Nexus switch)

Layer 3 EtherChannel
- Switch1(config)#interface range GigabitEthernet 1/0/1 - 2
- Switch1(config-if-range)#no switchport
- Switch1(config-if-range)#channel-group 1 mode | active | auto | desirable | on | passive
- Switch1(config)#interface port-channel 1
- Switch1(config-if)#ip address 192.168.0.1 255.255.255.252
- Switch1(config-if)#no shutdown
