import socket
import struct
host = "192.168.5.6"
port = 5610
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print "connected by", addr
msz= struct.pack('hhl', 1, 2, 3) 
conn.send(msz)
conn.close()
