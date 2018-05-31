import socket
import struct
import binascii
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 8)
while True:
	try:
		pkt  = s.recvfrom(2048)
		ethhead = pkt[0][0:14]
		eth = struct.unpack("!6s6s2s",ethhead)
		print "*"*50
		print "--------Ethernet Frame--------"
		print "Source MAC --> Destination MAC"
		print binascii.hexlify(eth[1]),"-->",binascii.hexlify(eth[0])
		print "-----------IP------------------"
		num=pkt[0][14].encode('hex')
		ip_length = (int(num)%10)*4
		ip_last_range = 14+ip_length
		ipheader = pkt[0][14:ip_last_range]
		ip_hdr = struct.unpack("!12s4s4s",ipheader)
		print "Source IP-->  Destination IP"
		print socket.inet_ntoa(ip_hdr[1]),"-->", socket.inet_ntoa(ip_hdr[2])
		print "---------TCP----------"
		tcpheader = pkt[0][ip_last_range:ip_last_range+20]

		tcp_hdr = struct.unpack("!HH9sB6s",tcpheader)
		print "Source Port--> Destination Port"
		print tcp_hdr[0],"-->", tcp_hdr[1]
		flag1 =tcp_hdr[3]
		print flag1
		str1 = bin(flag1)[2:].zfill(8)	
		flag1 = ''
		if str1[0]== '1':
			flag1 = flag1+"CWR "
		if str1[1] == '1':
			flag1 = flag1+ "ECN Echo "
		if str1[2] == '1':
			flag1 = flag1 + "Urgent "
		if str1[3]== '1':
			flag1 = flag1+ "Ack "

		if str1[4]== '1':
			flag1 = flag1+"Push "
		if str1[5] == '1':
			flag1 = flag1+ "Reset "
		if str1[6] == '1':
			flag1 = flag1 + "Sync "
		if str1[7]== '1':
			flag1 = flag1+ "Fin "
		
		print "Flag", flag1
	except Exception as e :
		print e
	
	


