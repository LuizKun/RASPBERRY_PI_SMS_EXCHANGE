import serial
import time
ser = serial.Serial('/dev/ttyAMA0',2400,timeout=1)
ser.flush()
ser.write('atd01674633840;\r')
print "Dang goi dien so : 01674633840"
time.sleep(2)
ser.read(9999)
time.sleep(10)
ser.close()
