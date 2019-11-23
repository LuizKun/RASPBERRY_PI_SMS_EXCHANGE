import serial
from serial import Serial
from time import sleep

ser = Serial("/dev/ttyAMA0",2400, timeout=1)

data2 = ser.write("at\r")
data = ser.read(9999)
if len(data) > 0:
        print 'Got:', data
sleep(0.5)
sdt = "01638800267"
ser.write('at+cmgs="01674633840"'+'\r\n')
rcv = ser.read(9999)
print rcv
sleep(1)

#rcv1 = rcv[:7]
#print rcv1

#a = "anh yeu em"
#while a != "a":
#	print a
#	sleep(2)


#while rcv1 == "at+cmgs":
#	rcv1 = ser.read(9999)
#	print "aaaaaaa"
#	rcv1 = "at+cmgs"

#if rcv1 == "at+cmgs":
#	print "anh yeu em"
#ser.write('hello world, sms from raspberry Pi! tks you.'+'\r')
rcv = ser.read(9999)
print rcv
ser.write("\x1A")

sleep(2)
rcv = ser.read(9999)
print rcv
ser.close()
