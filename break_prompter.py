#!/usr/bin/python

#this program's intended use is for AEA stage managers.  I want it to take the reheasal start and
#end times and return possible break schedules, including meal breaks.  AEA rules are as follows:
#5 minute break after 55 minutes of rehearsal OR
#10 minute break after 80 minutes of rehearsal AND
#if rehearsal is more than 5 hours, there MUST be a meal break of at least 1 hour.

print "Welcome to the AEA rehearsal scheduler!"
import time
time.sleep(0.5)
print "Please use a 24-hour clock system while inputting your times."
time.sleep(1)
print "When does rehearsal start?"
starth = int(raw_input("Hour: "))
startm = int(raw_input("Minute: "))
print "When does rehearsal end?"
endh = int(raw_input("Hour: "))
endm = int(raw_input("Minute: "))

#having a bit of difficulty working out the minute representation here.... Let's see.

starttotal = starth*60 + startm
endtotal = endh*60 + endm

print starttotal #just checking
print endtotal #just checking

#------------------- end of part one ---------------------

if (endtotal - starttotal) < 300:
    #use a while loop here once I figure out more shit
    #let's do 5/55 first
    #I'm working on doing this with a function
    break10 = starttotal + 55  #start time + 55 minutes = beginning of break
    break15 = break10 + 5  #beginning of break + 5 minutes = end of break   

        


