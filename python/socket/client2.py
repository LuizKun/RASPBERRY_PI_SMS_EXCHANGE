import socket
name = socket.gethostname()
print name
ip = socket.gethostbyname(name)
print ip
client=socket.socket()
client.connect(ip,135)
client.send("hello server")

client.recv(1024)
