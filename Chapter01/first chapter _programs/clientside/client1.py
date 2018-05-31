import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.5.6"
port = 5610
s.connect((host,port))
#print s.recv(1024)

s.send("Hello Server")
s.close()
