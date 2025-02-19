Access Control List Overview
- ACL’s are supported on both routers and switches
- By default a router/switch will allow all traffic to pass between its interfaces
- ACL’s are also used in other software policies when traffic has to be identified : QoS, NAT
- Access Control Lists are made up of Access Control Entries which are a series of permit or deny rules
- R1(config)# access-list 100 deny tcp 10.10.10.10 0.0.0.0 gt 49151 10.10.50.10 0.0.0.0 eq 23
- R1(config)# access-list 100 permit tcp 10.10.10.0 0.0.0.255 gt 49151 10.10.50.10 0.0.0.0 eq 23

Standard, Extended and Named ACLs
- Standard ACLs reference the source address only, default wildcard mask for a Standard ACL is 0.0.0.0 : 1 – 99, 1300-1999
- R1(config)# access-list 1 deny 10.10.10.10 0.0.0.0
- R1(config)# access-list 1 permit 10.10.10.0 0.0.0.255

- Extended ACLs check based on the protocol, source address, destination address, and port number, no default wildcard : 100 - 199, 2000-2699
- R1(config)# access-list 100 deny tcp 10.10.10.10 0.0.0.0 gt 49151 10.10.50.10 0.0.0.0 eq 23
- R1(config)# access-list 100 permit tcp 10.10.10.0 0.0.0.255 gt 49151 10.10.50.10 0.0.0.0 eq telnet

- Named ACLs
- R1(config)#ip access-list standard Flackbox-Demo
- R1(config-std-nacl)#deny 10.10.10.10 0.0.0.0
- R1(config-std-nacl)#permit 10.10.10.0 0.0.0.255

ACL Syntax
- Use TCP or UDP if you want the ACE to apply to traffic for a particular application between a source and destination address
- R1(config)#access-list 100 deny tcp 10.10.10.0 0.0.0.255 10.10.50.0 0.0.0.255 eq 80
- Use IP if you want the ACE to apply to all traffic between a source and destination address
- R1(config)#access-list 100 deny ip 10.10.10.0 0.0.0.255 10.10.50.0 0.0.0.255

- R1(config)#access-list 100 permit tcp 10.10.10.10 0.0.0.0
- R1(config)#access-list 100 permit tcp host 10.10.10.10
- R1(config)#access-list 100 permit tcp 0.0.0.0 255.255.255.255
- R1(config)#access-list 100 permit tcp any

- R2#sh access-lists 100

ACL Operations
- ACLs are applied at the interface level with the Access-Group command
- You can have a maximum of one ACL per interface per direction
- R1(config)# interface GigabitEthernet0/1
- R1(config-if)# ip access-group 100 out
- R1(config-if)# ip access-group 101 in
- R3#show ip interface f1/0 | include access list

- Injecting ACEs in an existing ACL
- R1(config)#ip access-list extended 110
- R1(config-ext-nacl)#15 deny tcp host 10.10.10.11 host 10.10.50.10 eq telnet

- Explicit Deny/Permit
- R1(config)# access-list 1 deny any log
- R1(config)# access-list 1 permit any

- ACL’s applied to an interface do not apply to traffic which originates from the router itself
