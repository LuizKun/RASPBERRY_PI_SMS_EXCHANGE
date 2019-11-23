
import serial
from serial import Serial
from time import sleep

ser = Serial("/dev/ttyAMA0",2400, timeout=1)

data2 = ser.write("at\r")
data = ser.read(2)
sleep(1)
print 'Got:', data

#doc sms ngan thu 1
ser.write('at+cmgf=3\r\n')
rcv = ser.read(9999)
sleep(1)
print rcv
sleep(1)

ser.write('at+cnmi=2,1\r\n')
rcv = ser.read(9999)
sleep(1)
print rcv
sleep(1)

