DHCP snooping
- (Routeur1)config-if# ip helper-address 10.10.20.10

- (SW1)config# ip dhcp-snooping
- (SW1)config# ip dhcp-snooping vlan 10 
- SW1(config)#int f0/1
- SW1(config-if)# ip dhcp-snooping trust
- When DHCP Snooping is enabled, DHCP Server responses are dropped if they don’t arrive on a trusted port.

DAI Dynamic ARP Inspection
- When you enable DHCP snooping, the switch inspects the DHCP traffic and keeps track of which IP addresses were assigned to which MAC addresses
- SW1(config)#int f0/1
- SW1(config-if)#ip arp inspection trust : don't block traffic from DHCP server !!!
- SW1(config)#ip arp inspection vlan 10
- DAI is not performed on trusted ports. Enable this for non DHCP clients.

802.1x Identity Based Networking
- When 802.1X is enabled, only authentication traffic is allowed on switch ports until the host and user are authenticated
- When the user has entered a valid username and password, the switch port transitions to a normal access port in the relevant VLAN
- Supplicant/Authenticator/Authentication Server

Port Security
- Port Security enables an administrator to specify which MAC address or addresses can send traffic in to an individual switch port.
- SW1(config)#int f0/2
- SW1(config-if)#switchport port-security
- SW1#show port-security interface f0/2
- You have three options when an unauthorised MAC address sends traffic in to the port : Shutdown (Default)/Protect/Restrict
- SW1(config)#int f0/2
- SW1(config-if)# switchport port-security violation protect
- SW1(config-if)# switchport port-security violation restrict
- SW1(config)# errdisable recovery cause psecure-violation
- SW1(config)# errdisable recovery interval 600

- SW1(config)# interface f0/2
- SW1(config-if)# switchport port-security maximum 2
- SW1(config)# interface f0/10
- SW1(config-if)# switchport port-security
- SW1(config-if)#switchport port-security mac-address 1111.2222.3333
- SW1(config-if)# switchport port-security maximum 1

- Manually adding the MAC addresses is not a scalable solution. Sticky MAC addresses add the learned MAC address to the running configuration. Save to the startup config to make them permanent
- SW1(config)# interface f0/2
- SW1(config-if)# switchport port-security
- SW1(config-if)# switchport port-security mac-address sticky

- SW1#show port-security address : Verify Port Security Addresses
- SW1#show port-security : View Summary Information
