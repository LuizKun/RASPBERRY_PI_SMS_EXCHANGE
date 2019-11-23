import serial
from serial import Serial
import time
import datetime
from time import sleep
from time import gmtime, strftime

while True:
        kt = open('/var/www/html/system/check.txt')
        kiemtra = kt.read(1)
        kt.close()

        #neu kiem tra co nhan nut submit thi thuc hien lenh
        if kiemtra == '1':
                #doc thong bao
                thongbao = open('/var/www/html/system/thongbao.txt')
                textthongbao = thongbao.read()
                thongbao.close()
		print "-------------"
                print textthongbao
		print "-------------"

		sdtsend = open('/var/www/html/system/sdtsend.txt')
		sdt_send = str(sdtsend.readline())
		sdtsend.close()

                ser = Serial("/dev/ttyAMA0",2400, timeout=1)
		sleep(1)
		guiat = ser.write("at\r")
		sleep(0.5)
		readat = ser.read(9999)
                with open("/var/www/html/"+sdt_send, mode="r") as my_file:
                        for line in my_file:
                                sdt = str(line[:-2])
                                print sdt
                                sleep(1)
				
				#gui sms
				data = ser.read(9999)
				sleep(1)
				if len(data) > 0:
				        print 'Got:', data
				ser.write('at+cmgs="'+sdt+'"\r\n')
				rcv = ser.read(9999)
				sleep(1)
				print rcv
				ser.write(textthongbao)
				rcv = ser.read(9999)
				sleep(1)
				print rcv
				ser.write("\x1A")
				sleep(1)
                ser.close()
                print "-------------\nDa gui xong sms"

                time = open('/var/www/html/system/time.txt','w+')
		now = datetime.datetime.now()
		timedagui = now.strftime("%Y-%m-%d %H:%M")
		print timedagui
		time.write(timedagui)
                time.close()

                kt = open('/var/www/html/system/check.txt','w')
                kt.write("0")
                kt.close()
	else:
		print "Dang cho lenh..."
		sleep(2)
		print "..."
		sleep(2)
