import socket
import sys
HOST = ''	# Symbolic name meaning all available interfaces
PORT = 2332	# Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
	s.bind((HOST, PORT))
except socket.error , msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
print 'Socket bind complete'
s.listen(1)
while True:
	print "socket now listening"

	conn,addr = s.accept()
	print 'connected with'+addr[0]+':'+str(addr[1])
	data = conn.recv(1024)
	data2 = "anh yeu em nhieu lam"
	conn.sendall(data2)
conn.close()
s.close()
