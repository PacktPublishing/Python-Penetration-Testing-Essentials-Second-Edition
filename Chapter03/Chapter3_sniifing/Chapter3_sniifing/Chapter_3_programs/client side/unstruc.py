import socket
import struct 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.5.6"
port = 5610
s.connect((host,port))
msg= s.recv(1024)
print msg
print struct.unpack('hhl',msg)
s.close()
