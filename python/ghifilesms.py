import serial
import time

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
		time.sleep(0.5)
		nhansms.close()


sms = TextMessage("0964219940","hello boss, i'm raspberry pi!","25/08/2016 13:49")
sms.writefile()
print "\nDa gui tin nhan thanh cong"

