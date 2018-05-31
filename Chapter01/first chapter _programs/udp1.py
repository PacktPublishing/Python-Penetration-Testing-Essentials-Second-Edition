import socket
host = "192.168.5.6"
port = 5610
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
data, addr = s.recvfrom(1024)
print "recevied from ",addr
print "obtained ", data
s.close()
