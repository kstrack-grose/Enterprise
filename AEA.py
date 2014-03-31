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
from datetime import datetime
from datetime import timedelta

#FUNCTIONS
	#DAY FUNCTION
def day():
	dprompt = raw_input("Day of the month: ")
	if len(dprompt) < 2:                 #convert to two digits
		dprompt = "0"+dprompt 
	while dprompt.isalnum() and not dprompt.isdigit() or len(dprompt) > 2 or int(dprompt) < 1 or int(dprompt) > 31:
		dprompt = raw_input("Please try again: ") 
	day = int(dprompt) 
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
	if ampm == "AM" and hprompt == 12:
		hprompt == 00 #midnight
	if ampm == "PM":
		if hprompt != 12:
			hprompt = hprompt + 12 
		else:
			hprompt == "12" #NOON 
	while ampm != "PM" and ampm != "AM":
		ampm = raw_input("Please try AM/PM again: ").upper()
	hour =  int(hprompt)
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
	minute = int(mprompt)
	return minute

	#5/55 function--I'm wondering how to make a while loop save each iteration in a different variable...
# def 5out55(starttime, endtime):
#	timeCursor = starttime
#	while timeCursor <= (endtime - timedelta(minutes = 55)):
		
#VARIABLES
it = ""                                                                 # 'it' is for iteration.


#WELCOME MESSAGE HERE


now = datetime.now() #sets current dates 

print "Please enter the rehearsal start time."	
	#datetime for start:
# start =  datetime(now.year, now.month, day(), hour(), minute())           ADD BACK IN
start = datetime(now.year, now.month, 1, 12, 00)

print "\nPlease enter the rehearsal end time:"
	#datetime for end:
# end = datetime(now.year, now.month, day(), hour(), minute())              ADD BACK IN
end = datetime(now.year, now.month, 1, 16, 30)

#confirm start/end times with user:
print "\nPlease confirm your rehearsal's start time:"
print start
# startChoice = raw_input("Was that correct?  Yes or no: ")                  ADD BACK IN vv
# if startChoice.lower()[0] == "n":
# 	print "\nPlease enter your start time again. \n"
#	start =  datetime(now.year, now.month, day(), hour(), minute()) 
#^basically start from beginning of start inputs


print "\nPlease confirm your rehearsal's end time:"
print end
# endChoice = raw_input("Was that correct?  Yes or no: ")                  ADD BACK IN vv
# if endChoice.lower()[0] == "n":
#	print "\nPlease enter your end time again. \n"
#	end = datetime(now.year, now.month, day(), hour(), minute()) 
#^basically start from beginning of end inputs


#break times BIAS
print "\nIn general, would you prefer to break \na) 5 minutes every 55 minutes \nor \nb) 10 minutes every 80 minutes? \n"
bias = raw_input("a or b: ")
bias = bias.lower()

totalDelta = end - start
totalMin = totalDelta.total_seconds()//60
print "total delta", totalDelta
print "total min", totalMin


nowTime = start
print "nowTime =", start

#NOW BEGINS THE THREE OPTIONS BY MEAL BREAK
#first one: if rehearsal <= 5 hours
#help just none of this works

if totalMin < 300:
	if bias == 'a':
		while start < end:
			it += 's' 				        # s for start                              
#the idea here is to create a self-accruing variable that can store as many runs of the while loop as it needs to.
#shit wait no it's not going to work.			
			run = datetime.timedelta(minutes = 55)
			nowtime = nowtime + run
			print nowtime                           #TAKE OUT LATER			
			it += 'e'					# e for end
			pause = datetime.timedelta(minutes = 5)				
			nowtime = nowtime + pause
			print nowtime                           #TAKE OUT LATER			




	if bias == 'b':
		print "Sorry, I'm not there yet!"
