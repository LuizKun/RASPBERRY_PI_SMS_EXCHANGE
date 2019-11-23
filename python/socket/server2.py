import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = 135
address = (ip,port)
server.bind(address)
server.listen(1)
print ("listening on ",ip," : ",port)
client.addr = server.accept()
print ("got a connection from",addr[0],":",addr[1] )
while True:
	client.cend("cmm")
	data = client.recv(1024)
	print ("received",data,"from client")
	print "processing data"
	if (data == "hello server"):
		client.send("hello client");
		print "da xu ly xong"+"dang doi tin nhan"
	elif(data == "disconect"):
		client.send("goodbye");
		client.close()
		break
	else:
		client.send("invalid data")
		print "processing done"
