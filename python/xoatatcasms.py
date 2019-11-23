import serial
from serial import Serial
from time import sleep

ser = Serial("/dev/ttyAMA0",2400, timeout=1)

data2 = ser.write("at\r")
data = ser.read(2)
sleep(1)
print 'Got:', data

#doc sms ngan thu 1
ser.write('at+cmgda="DEL ALL"\r\n')
rcv = ser.read(9999)
ser.close()
