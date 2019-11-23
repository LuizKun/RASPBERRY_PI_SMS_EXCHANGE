import serial 
from serial import Serial
import time
from time import sleep

class TextMessage:
        def __init__(self, recipient="", message="",timenhan=""):
                self.recipient = recipient
                self.content = message
                self.thoigiannhan = timenhan

        def writefile(self):

                filename = (""+self.recipient+ ".txt")
                print filename

                nhansms = open('/var/www/html/sms/'+filename,'w+')
                nhansms.write(self.recipient+'\n'+self.content+'\n'+self.thoigiannhan)
                sleep(0.5)
                nhansms.close()


ser = Serial("/dev/ttyAMA0",2400, timeout=1)

data2 = ser.write("at\r")
data = ser.read(9999)
print 'Dang Khoi Dong \n', data
sleep(1)
dem = 0
i = 1

while True:
	if i == 1:	
		ser.write('at+cmgr=1\r\n')
		sms1 = ser.read(9999)
		sleep(1)
		print sms1
		sleep(1)

		docsms1 = sms1[13:15]#kiem tra co sms hay khong
		if docsms1 == "OK":
        		print "Khong co SMS ngan thu : 1"
			sleep(1) #do nothing doi sms
		else:
			cmti = sms1[3:7]
			if cmti == "CMTI":
	        		#print rcv[0:34]
        			print "-------------"
        			print "so dien thoai :"
				sdt = sms1[52:64]
        			print (sms1[52:64]+'\n' )#cat so dien thoai can dung

        			print "Thoi gian nhan :"
				thoigian = sms1[70:84]
        			print (sms1[70:84]+'\n')

        			print "noi dung sms:"
        			noidungsms1 = sms1[93:]
				noidung = noidungsms1[:-8]
        			print noidungsms1[:-8]
				
				#ghi SMS, time, noidung vao file
				sms = TextMessage(sdt,noidung,thoigian)
				sms.writefile()


				#xoa sms vi tri thu 1
				ser.write('at+cmgd=1\r\n')
				sleep(0.5)
				xoasms1 = ser.read(9999)
				print "da xoa sms ngan thu : 1 \n"
				sleep(1)
				dem = 1
				i = i + 1
			else:
				#print rcv[0:34]
                                print "-------------"
                                print "so dien thoai :"
				sdt = sms1[35:47]
                                print (sms1[35:47]+'\n' ) #sdt gui sms

                                print "Thoi gian nhan :"
				thoigian = sms1[53:67] #thoi gian nhan sms
                                print (sms1[53:67]+'\n')

                                print "noi dung sms:"
                                noidungsms1 = sms1[74:]
				noidung = noidungsms1[:-8] #noi dung sms
                                print noidungsms1[:-8]

                                sms = TextMessage(sdt,noidung,thoigian)
                                sms.writefile()

                                #xoa sms vi tri thu 1
                                ser.write('at+cmgd=1\r\n')
                                sleep(0.5)
                                xoasms1 = ser.read(9999)
                                print "da xoa sms ngan thu : 1 \n"
                                sleep(1)
                                dem = 1
                                i = i + 1
		sleep(2)		

	if dem == 1:
		#doc sms tu ngan thu 2
		ser.read(9999)
		sleep(0.5)
		ser.write('at+cmgr='+str(i)+'\r\n')
		rcv = ser.read(9999)
		#sleep(1)
		#print rcv
		sleep(1)
		docsmsi = rcv[13:15]
		if docsmsi == "OK":
        		print ('Khong co SMS ngan thu : '+str(i))
			dem = 0
			i = 1
		else:
			cmti = sms1[3:7]
                        if cmti == "CMTI":
                                #print rcv[0:34]
                                print "-------------"
                                print "so dien thoai :"
				sdt = rcv[52:64]
                                print (rcv[52:64]+'\n' )#cat so dien thoai can dung

                                print "Thoi gian nhan :"
				thoigian = rcv[70:84]
                                print (rcv[70:84]+'\n')

                                print "noi dung sms:"
                                noidungsmsi = rcv[93:]
				noidung = noidungsmsi[:-8]
                                print noidungsmsi[:-8]

                                sms = TextMessage(sdt,noidung,thoigian)
                                sms.writefile()


                                #xoa sms vi tri thu 1
                                ser.write('at+cmgd=1\r\n')
                                sleep(0.5)
                                xoasmsi = ser.read(9999)
                                print "da xoa sms ngan thu : 1 \n"
                                sleep(1)
                                dem = 1
                                i = i + 1
			else:
	        		#print rcv[0:34]
        			print "-------------"
        			print "so dien thoai :"
				sdt = rcv[35:47]
        			print rcv[35:47] #cat so dien thoai can dung

        			print "Thoi gian nhan :"
				thoigian = rcv[53:67]
        			print rcv[53:67]

        			print "noi dung sms:"
        			a = rcv[74:]
				noidung = a[:-8]
        			print a[:-8]

                                sms = TextMessage(sdt,noidung,thoigian)
                                sms.writefile()

				#xoa sms vi tri thu i
				ser.write('at+cmgd='+str(i)+'\r\n')
				rcv = ser.read(9999)
				print ('da xoa sms ngan thu :'+str(i)+'\n')
				sleep(1)
				i = i + 1
ser.close()

