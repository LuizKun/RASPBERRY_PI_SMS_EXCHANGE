import socket
import RPi.GPIO as GPIO


HOST = '192.168.137.103'
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#managing error exception
try:
	s.bind((HOST, PORT))
except socket.error:
	print 'Bind failed '
#s.listen(5)
#print 'Socket awaiting messages'
#(conn, addr) = s.accept()
#print 'Connected'

# awaiting for message
while True:
	s.listen(1)
	print 'Socket awaiting messages'
	(conn, addr) = s.accept()
	print 'Connected'

	data = conn.recv(1024)
	print 'I sent a message back in response to: ' + data
	reply = ''

	# process your message
	if data == 'Hello':
		reply = 'Hi, back!'
		print "Led 1 on"
	elif data == 'This is important':
		reply = 'OK, I have done the important thing you have asked me!'
	#and so on and on until...
	elif data == 'quit':
		conn.send('Terminating')
		break
	else:
		reply = 'Unknown command'
	# Sending reply
	conn.send(reply)
conn.close() # Close connections
