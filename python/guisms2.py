import serial
from serial import Serial
import time
import datetime
from time import sleep
from time import gmtime, strftime

class TextMessage:
        def __init__(self, recipient="", message=""):
            self.recipient = recipient
            self.content = message

#        def setRecipient(self, number):
#            self.recipient = number

#        def setContent(self, message):
#            self.content = message

        def connectPhone(self):
            self.ser = serial.Serial('/dev/ttyAMA0',2400,timeout=2)
            time.sleep(1)

        def sendMessage(self):
            self.ser.write('at\r')
            time.sleep(1)
            rcv = self.ser.read(9999)
            print (rcv+"\n")

            #self.ser.write('at+cmgf=1\r')
            #time.sleep(1)
            #rcv = self.ser.read(9999)
            #print rcv

            self.ser.write('''at+cmgs="''' + self.recipient + '''"\r''')
            time.sleep(1)
            rcv = self.ser.read(9999)
            print rcv

            self.ser.write(self.content + "\r")
            time.sleep(1)
            rcv = self.ser.read(9999)
            print rcv

            self.ser.write(chr(26))
            time.sleep(1)
            rcv = self.ser.read(9999)
            print rcv

        def disconnectPhone(self):
            self.ser.close()
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
                print textthongbao

		#doc tap tin sdt can gui
		sdtsend = open('/var/www/html/system/sdtsend.txt')
		sdt_send = str(sdtsend.readline())
		sdtsend.close()

                #ser = Serial("/dev/ttyAMA0",2400, timeout=1)
                #with open("/var/www/html/upload/sodienthoai.txt", mode="r") as my_file:
                with open("/var/www/html/"+sdt_send, mode="r") as my_file:
                        for line in my_file:
                                sdt = str(line[:-2])
				#sdt = str(line.rstrip("\n"))
                                print sdt
                                sleep(1)
				sms = TextMessage(sdt,textthongbao)
				sms.connectPhone()
				sms.sendMessage()
				sms.disconnectPhone()
                #ser.close()
                print "Da gui xong sms"
                #gui xong 1 sms toi sdt => cap nhat ghi tiep vao file, hien thi tren web
                time = open('/var/www/html/system/time.txt','w+')
		now = datetime.datetime.now()
		timedagui = now.strftime("%Y-%m-%d %H:%M")
		print timedagui
		time.write(timedagui)
                time.close()

                #gui xong sms den cac sdt thi => ghi gia tri "0" vao trong file, cho nut submit.
                kt = open('/var/www/html/system/check.txt','w')
                kt.write("0")
                kt.close()


