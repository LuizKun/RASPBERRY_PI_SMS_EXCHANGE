import datetime
from time import gmtime, strftime

now = datetime.datetime.now()
print strftime("%Y-%m-%d %H:%M:%S", gmtime())
print strftime("%a, %d %b %Y %X", gmtime())
print now.isoformat()
print now.strftime("%Y-%m-%d %H:%M")
