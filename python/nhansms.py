import serial
from serial import Serial
from time import sleep

ser = Serial("/dev/ttyAMA0",2400, timeout=1)

#data2 = ser.write("at\r")
#data = ser.read(2)
#sleep(1)
#print 'Got:', data

#doc sms ngan thu 1
ser.read(9999)
sleep(0.5)
ser.write('at+cmgr=3'+'\r\n')
rcv = ser.read(9999)
sleep(1)
print rcv
sleep(1)
kt = rcv[13:15]
if kt == "OK":
	print "Khong co SMS"
else:
	#print rcv[0:34]
	print "-------------"
	print "so dien thoai :"
	print rcv[35:47] #cat so dien thoai can dung
	print "Thoi gian nhan :"
	print rcv[53:67]
	print "noi dung sms:"
	a = rcv[74:]
	print a[:-8]

#xoa sms vi tri thu 1
#ser.write('at+cmgd=2\r\n')
#rcv = ser.read(9999)
#print "da xoa sms"

sleep(1)
ser.close()
