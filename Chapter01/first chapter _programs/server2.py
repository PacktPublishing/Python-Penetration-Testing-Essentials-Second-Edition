import socket 
host = "192.168.1.46"
port = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)
while True:
	conn, addr = s.accept()
	print addr, "Now Connected"
	msz = raw_input("Enter the message  ")
	conn.send(msz)
	print conn.recv(1024)
	conn.close()
