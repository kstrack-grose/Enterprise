#!/usr/bin/python

import time

x = 1 #initialize variable
while x <= 100:
        if (x%3 != 0) and (x%5 != 0): #if x is divisible by neither 3 or 5:
                print x
                time.sleep(.1) #just for a pretty output
                x += 1
        elif (x%3 == 0) and (x%5 != 0): #if x is divisible by 3 but not 5
                print "Crackle"
                time.sleep(.1)
                x += 1
        elif (x%3 != 0) and (x%5 == 0): #if x is divisble by 5 but not 3
                print "Pop"
                time.sleep(.1)
                x += 1
        elif (x%3 == 0) and (x%5 == 0): #if x is divisible by 3 and 5!
                print "CracklePop"
                time.sleep(.1)
                x += 1
