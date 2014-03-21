#!/usr/bin/python

#This is a program that, given rehearsal start and end times, will produce the proper
#AEA-mandates breaks.  The rules for those breaks are as follows:
#For every 55 minutes of rehearsal, 5 minutes of break (known as 5/55)
#or
#For every 80 minutes  of rehearsal, 10 minutes of break (10/80)
#and
#If rehearsal is more than 5 hours, there must be a meal break
#of at least 1 hour.

#imports:
import time
import datetime

#FUNCTIONS
	#DAY FUNCTION
def day():
	dprompt = raw_input("Day of the month: ")
	if len(dprompt) < 2:                 #convert to two digits
		dprompt = "0"+dprompt 
	while dprompt.isalnum() and not dprompt.isdigit() or len(dprompt) > 2 or int(dprompt) < 1 or int(dprompt) > 31:
		dprompt = raw_input("Please try again: ") 
	day = dprompt 
	return day

	#HOUR FUNCTION
def hour():
	hprompt = raw_input("Hour: ")
	if len(hprompt) < 2:
		hprompt = "0"+hprompt  #convert to two digits
	while hprompt.isalnum() and not hprompt.isdigit() or len(hprompt) > 2:
		hprompt = raw_input("Please try again: ")
	while int(hprompt) < 1 or int(hprompt) > 12:
		hprompt = raw_input("Please try again: ")
	
	hprompt = int(hprompt) #to convert to 24 hour clock system
	ampm = raw_input("AM or PM? ")
	ampm = ampm.upper()
	if ampm == "AM" and hprompt != 12:
		hprompt = str(hprompt) #no need to add hours but do need to convert back to string
	if ampm == "PM" and hprompt != 12:
		hprompt = str(hprompt + 12) 
	if ampm == "PM" and hprompt == 12:
		ampm == "12" #NOON 
	while ampm == "AM" and hprompt == 12:  #if midnight
		print "Please do not enter midnight exactly.\nA minute ahead or behind will give \n a good approximate."
		hprompt = raw_input("Hour: ")
	while ampm.isalnum() and not ampm.isalpha() or len(ampm) < 2 or len(ampm) > 2:
		hprompt = raw_input("Please try again: ")
	hour =  str(hprompt)
	return hour

	#MINUTE FUNCTION
def minute():	
	mprompt = raw_input("Minute: ")
	if len(mprompt) < 2:
		mprompt = "0" + mprompt
	if int(mprompt) < 0 or int(mprompt) > 59:
		mprompt = raw_input("Please try again: ")
	while mprompt.isalnum() and not mprompt.isdigit() or len(mprompt) > 2:
		mprompt = raw_input("Please try again:  ")	
	minute = mprompt
	return minute




#WELCOME MESSAGE HERE

print "Please enter the rehearsal start time."	

	#concatenate start:
start = day() + " " + hour() + " " + minute()

	#concatenate end:
print "Please enter the rehearsal end time:"
end = day() + " " + hour() + " " + minute()

starttime = time.strptime(start, "%d %H %M")
endtime = time.strptime(end, "%d %H %M")


#break times BIAS
print "In general, would you prefer to break a) 5 minutes every 55 minutes \n or b) 10 minutes every 80 minues?"
bias = raw_input("a or b: ")
bias = bias.lower()

print "start:", start
print "end:", end

delta = starttime - endtime
print delta
