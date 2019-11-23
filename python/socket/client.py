import socket
s = socket.socket()
server = '127.0.0.1'
port = 567
s.connect((server,port))
print (s.recv(1024))
s.close()

