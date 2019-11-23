import serial
import time
ser = serial.Serial('/dev/ttyAMA0',2400,timeout=1)
ser.flush()
while True:
	ser.write('ath\r')
	time.sleep(2)
	a = ser.read(9999)
	print a
	time.sleep(10)
ser.close()

