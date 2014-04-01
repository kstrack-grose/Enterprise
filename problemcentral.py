#!/usr/bin/python

#imports
import time
import datetime
from datetime import datetime
from datetime import timedelta

#start/end
start = datetime(2014, 4, 1, 2, 00)
end = datetime(2014, 4, 1, 8, 30)

#just to check in, visually
print "start at", start
print "end at", end

#create caches of time, I guess
totalTime = end - start
totalMin = totalTime.total_seconds()//60

#again, checking in
print "total time is", totalTime
print "total minutes:", totalMin

#next task; to iterate through a while loop
#and my real challenge is to save a bunch of times
#as beginning and ends of breaks
#so
#help?
#re: iterating through changing variables
#variables
time = start
run = timedelta(0, 0, 0, 0, 55)
breakk = timedelta(0, 0, 0, 0, 5)

#again to check it out
print "run", run
print "break", breakk

while time < end:
    startbreak1 = time + run
    print "startbreak1", startbreak1
    endbreak1 = startbreak1 + breakk
    print "endbreak1", endbreak1
    time = endbreak1
#and then iterate through, saving things as startbreak2 and endbreak2 and such on.  how?
