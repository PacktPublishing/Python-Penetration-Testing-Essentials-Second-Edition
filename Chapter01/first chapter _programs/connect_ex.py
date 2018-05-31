import socket

rmip =raw_input("192.168.5.6")

st1= raw_input("Enter first port ")
en1 = raw_input("Enter last port ")



for port in xrange(st1, en1)
	sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	
	result = sock.connect_ex((rmip,port))
	sock.setdefaulttimeout(1)
	if result == 0:
		print port, "--> Open"
	sock.close()

