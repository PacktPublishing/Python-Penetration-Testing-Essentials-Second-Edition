import socket
from datetime import datetime
import ping
import struct
import binascii
from threading import Thread
import time

s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

net = raw_input("Enter the Network Address ")
net1= net.rsplit('.',1)
net2 = net1[0]+'.'
start1 = int(raw_input("Enter the Starting Number "))
end1 = int(raw_input("Enter the Last Number "))
end1 =end1+1

seq_ip = []
total_ip =end1-start1
tn =10  # number of ip handled by one thread
total_thread = total_ip/tn
total_thread=total_thread+1
threads= []
t1= datetime.now()

def send_ping(st1,en1):
	for each in xrange(st1,en1):
		try:
			ip = net2+str(each)
			ping.do_one(ip,1,32)
		except Exception as e :
			print "Error in send_ping", e
	
def icmp_sniff():
	s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 8)

	while True:
		pkt  = s.recvfrom(2048)
		num = pkt[0][14].encode('hex')
		ip_length = (int(num) % 10) * 4
		ipheader = pkt[0][14:14+ip_length]
		icmp_h =pkt[0][14+ip_length]
		ip_hdr = struct.unpack("!8sBB2s4s4s",ipheader[:20])
		icmp_hdr = struct.unpack("!B",icmp_h)
		if(ip_hdr[2]==1) and (icmp_hdr[0]==0):
			ip = socket.inet_ntoa(ip_hdr[4])
			ip1= ip.rsplit('.',1)
			list_temp = [ip1[1].zfill(3),ip]
			seq_ip.append(list_temp)
	
scan_thread = Thread(target=icmp_sniff)
scan_thread.setDaemon(True)
scan_thread.start()
st1 = start1

try:
    for i in xrange(total_thread):
		en = st1+tn
		if(en >end1):
			en =end1
		ping_thread = Thread(target=send_ping,args=(st1,en,) )
		ping_thread.start()
		threads.append(ping_thread)
		st1 =en
		
except Exception as e :
     print "Error in Thread", e

for t in threads:
    t.join()
time.sleep(1)
seq_ip.sort(key=lambda x: int(x[0]))
print "S.no\t","IP"
for each in seq_ip:
	print each[0]," ", each[1]

t2= datetime.now()
print "Time taken ", t2-t1



