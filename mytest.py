##coding=utf-8
import os
import time
def phtest():
   print "this is a test!"
print "测试"   
os.system("mkdir -p /home/phtest/ph")
print "time sleep 30s\n"
time.sleep(2)

print "another time sleep 60s"
time.sleep(2)

i=1
if i==1:
   print "test is ok!"
else:
   print "test is fail!"
