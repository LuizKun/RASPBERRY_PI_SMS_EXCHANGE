import serial
from serial import Serial
import time
import datetime
from time import sleep
from time import gmtime, strftime

class TextMessage:
        def __init__(self, recipient="", message="",timenhan=""):
                self.recipient = recipient
                self.content = message
                self.thoigiannhan = timenhan

        def writefile(self):

                filename = (""+self.recipient+ ".txt")
#                print filename

                nhansms = open('/var/www/html/sms/noidung/'+filename,'w+')
                nhansms.write(self.content+'\n'+self.thoigiannhan)
                sleep(0.5)
                nhansms.close()

ser = Serial("/dev/ttyAMA0",2400, timeout=1)
sleep(1)
data2 = ser.write("at\r")
data = ser.read(9999)
print 'Dang Khoi Dong \n', data
sleep(1)
dem = 0
i = 1


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

                #ser = Serial("/dev/ttyAMA0",2400, timeout=1)
		#sleep(1)
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
#				rcv1 = rcv[:7]
#				print rcv1
				#neu dang gui sms ma co tin nha den
#				while rcv1 != "at+cmgs":
#					ser.write('at+cmgs="'+sdt+'"\r\n')
#					rcv = ser.read(9999)
#					print "co sms den"
#					sleep(1)
#					rcv1 = rcv[:7]

				ser.write(textthongbao)
				rcv = ser.read(9999)
				sleep(1)
				print rcv
				ser.write("\x1A")
				sleep(1)
                #ser.close()
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
                
	elif kiemtra == '0':
		
		#gui 1 sms
		ktsms = open('/var/www/html/sms/check.txt')
	        kiemtrasms = ktsms.read(1)
        	ktsms.close()
		if kiemtrasms == '1':
 	              	smstl = open('/var/www/html/sms/memory/sms.txt')
        	        noidungsms = smstl.read()
               		smstl.close()
                	print "-------------"
                	print noidungsms
                	print "-------------"

                	sdttl = open('/var/www/html/sms/memory/sdt.txt')
                	sdtsms = str(sdttl.readline())
                	sdttl.close()

                	#ser = Serial("/dev/ttyAMA0",2400, timeout=1)
                	#sleep(1)
                	guiat = ser.write("at\r")
               		sleep(0.5)
 			readat = ser.read(9999)
			data = ser.read(9999)
                        sleep(1)
                        ser.write('at+cmgs="'+sdtsms+'"\r\n')
                        rcv = ser.read(9999)
                        sleep(1)
                        print rcv
                        ser.write(noidungsms)
                        rcv = ser.read(9999)
                        sleep(1)
                        print rcv
                        ser.write("\x1A")
                        sleep(1)
	                
			ktsms = open('/var/www/html/sms/check.txt','w')
        	        ktsms.write("0")
                	ktsms.close()

		#nhan sms
	        if i == 1:
			ser.read(9999)
			sleep(0.5)	
        		ser.write('at+cmgr=1\r\n')
			sms1 = ser.read(9999)
			sleep(1)
			print sms1
			sleep(1)

			docsms1 = sms1[13:15]#kiem tra co sms hay khong
			noidungsms1 = ""
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

					#ghi vao file sms
	                                sms = TextMessage(sdt,noidung,thoigian)
        	                        sms.writefile()

                	                #xoa sms vi tri thu 1
                        	        ser.write('at+cmgd=1\r\n')
                               		sleep(0.5)
                                	xoasms1 = ser.read(9999)
                               		print "da xoa sms ngan thu : 1 \n"
                                	sleep(1)
                                	dem = 1 #neu co sms o ngan thu nhat, cho phep doc sms ngan thu 2.
                                	i = i + 1 #neu co sms ngan thu nhat, i = 2 de doc tin nhan ngan thu 2.
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


