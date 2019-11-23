from serial import Serial
from time import sleep

ser = Serial("/dev/ttyAMA0",2400, timeout=1)

data2 = ser.write("atz\r")
data = ser.read(9999)
if len(data) > 0:
        print 'Got:', data
sleep(0.5)
data2 = ser.write("ate1\r")
data = ser.read(9999)
if len(data) > 0:
        print 'Got:', data
sleep(0.5)
data2 = ser.write("at&w\r")
data = ser.read(9999)
if len(data) > 0:
        print 'Got:', data
sleep(0.5)

ser.close()


