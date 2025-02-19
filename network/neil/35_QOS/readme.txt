QoS Overview
- Traditional vs Converged Networks
- Congestion : Packets are arriving faster than they can be sent out > Packets wait in the queue to go out > Packets are sent out FIFO in the order they were received
- Mitigate Congestion : Mitigate Congestion or Use Quality of Service (The router recognises the voice packets and moves them to the front of the queue to minimise their delay)

Tagging
- Cost of Service : 3 bits in layer 2 802.1q header
- Differentiated Service Code Point : 6 bits in Type of Service Byte in layer 3 header
  - Switch should trust port
- Access Control List
- Network Based Application Recognition

Congestion management
- QoS queuing
- Class Based Weighted Fair Queue
- Low Latency Queue
- Modular QoS CLI
- Class Maps : config# class-map VOICE-PAYLOAD 
- Policy Maps : config# policy-map WAN-EDGE \ class voice payload
- Service Policy : config-if# service-policy WAN-EDGE out

Policing/Shapping
- shapping buffers any excess traffic
- policing drops or remarks excess traffic

