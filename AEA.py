#!/usr/bin/python

#This is a program that, given rehearsal start and end times, will produce the proper
#AEA-mandates breaks.  The rules for those breaks are as follows:
#For every 55 minutes of rehearsal, 5 minutes of break (known as 5/55)
#or
#For every 80 minutes  of rehearsal, 10 minutes of break (10/80)
#and
#If rehearsal is more than 5 hours, there must be a meal break
#of at least 1 hour.

#current bug:
#getting time after first meal (or second meal, probably
#to start at the end of the meal
#rather than the beginning of the rehearsal


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

	#how to divide between meal breaks
def timeToChunk(begin, stop):
	partialDelta = stop - begin
	partialMin = partialDelta.total_seconds()/60
	partialHours = partialMin/60
	intHours = int(partialHours//1)
	#checking in:
	print "checking in:"
	print "total delta", partialDelta
	print "total min", partialMin
	print "total hours", partialHours
	print "hours as an integer", intHours
	#and return intHours, so I can use it in the range
	return intHours

	#iterate through on a 5/55 basis
def iterateA(begin, stop):
	for x in range(0, timeToChunk(begin, stop)):
    		times.append("")
       		begin = begin + arun        
		times.append(["Start of break is", begin.strftime('%d, %r')])
        	begin = begin + abreak
       		times.append(["End of break is", begin.strftime('%d, %r')])
	for y in range(0, len(times)):
	        print times[y]

	#iterate through on a 10/80 basis
def iterateB(begin, stop):
	for x in range(0, timeToChunk(begin, stop)):
		times.append("")
		begin = begin + brun
		times.append(["Start of break is", begin.strftime('%d, %r')])
		begin = begin + bbreak
		times.append(["End of break is", begin.strftime('%d, %r')])
	for y in range(0, len(times)):
	        print times[y]


	#5/55 function--I'm wondering how to make a while loop save each iteration in a different variable...
# def 5out55(starttime, endtime):
#	timeCursor = starttime
#	while timeCursor <= (endtime - timedelta(minutes = 55)):
		
#VARIABLES and lists
times = [] 							      # list to hold breaks
arun = timedelta(0, 0, 0, 0, 55)                                      # runtime for 5/55
abreak = timedelta(0, 0, 0, 0, 5)                                     # breaktime for 5/55
brun = timedelta(0, 0, 0, 0, 80)                                      # runtime for 10/80
bbreak = timedelta(0, 0, 0, 0, 10)                                    # breaktime for 10/80

now = datetime.now() #sets current dates 

#WELCOME MESSAGE HERE



print "Please enter the rehearsal start time."	
	#datetime for start:
start =  datetime(now.year, now.month, day(), hour(), minute())          
#start = datetime(now.year, now.month, 1, 12, 00)

print "\nPlease enter the rehearsal end time:"
	#datetime for end:
end = datetime(now.year, now.month, day(), hour(), minute())             
#end = datetime(now.year, now.month, 1, 16, 30)

#confirm start/end times with user:
print "\nPlease confirm your rehearsal's start time:"
print start
startChoice = raw_input("Was that correct?  Yes or no: ")                
if startChoice.lower()[0] == "n":
 	print "\nPlease enter your start time again. \n"
	start =  datetime(now.year, now.month, day(), hour(), minute()) 
#^basically start from beginning of start inputs


print "\nPlease confirm your rehearsal's end time:"
print end
endChoice = raw_input("Was that correct?  Yes or no: ")                
if endChoice.lower()[0] == "n":
	print "\nPlease enter your end time again. \n"
	end = datetime(now.year, now.month, day(), hour(), minute()) 
#^basically start from beginning of end inputs


#break times BIAS
print "\nIn general, would you prefer to break \na) 5 minutes every 55 minutes \nor \nb) 10 minutes every 80 minutes? \n"
bias = raw_input("a or b: ")
bias = bias.lower()

#more variables:
totalDelta = end - start
totalMin = totalDelta.total_seconds()/60
totalHours = totalMin/60
intHours = int(totalHours//1)


#note: WHEN YOU MADE TIMETOCHUNK A FUNCTION, YOU REMOVED NOWTIME FROM IT. DO THAT INDIVIDUALLY.

#NOW BEGINS THE THREE OPTIONS BY MEAL BREAK
#first one: if rehearsal <= 5 hours

if totalMin < 300:
	begin = start
	stop = end
	#if 5/55 preference:
	if bias == 'a':
		iterateA(begin, stop)
		#^^this calls the iterate function and prints all of the break times
	if bias == 'b':
		iterateB(begin, stop)


if 300 <= totalMin < 600:
	#MEAL
	halfway = (end - start)/2 + start
	startmeal = halfway - timedelta(0, 0, 0, 0, 30)
	endmeal = halfway + timedelta(0, 0, 0, 0, 30)
	#aaand call iterate functions for before meal
	if bias == 'a':
		iterateA(start, startmeal)
	if bias == 'b':
		iterateB(start, startmeal)
	print "\nYour meal break will be from", startmeal, "to", endmeal
	#iterate
	if bias == 'a':
		iterateA(endmeal, end)
	if bias == 'b':
		iterateB(endmeal, end)


if 600 <= totalMin <900:
	#TWO MEALS
	third = (end - start)/3 + start
	startmeal1 = third - timedelta(0, 0, 0, 0, 30)
	endmeal1 = third + timedelta(0, 0, 0, 0, 30)
	#iterate
	if bias == 'a':
		iterateA(start, startmeal1)
	if bias == 'b':
		iterateB(start, startmeal1)
	#mealbreak!
	print "\nYour first meal break will be from", startmeal1, "to", endmeal1 
	secondThird = (2*(end-start))/3 + start
	startmeal2 = third - timedelta(0, 0, 0, 0, 30)
	endmeal2 = third + timedelta(0, 0, 0, 0, 30)
	#iterate
	if bias == 'a':
		iterateA(endmeal1, startmeal2)
	if bias == 'b':
		iterateB(endmeal1, startmeal2)
	#mealbreak!
	print "\nYour second meal break will be from", startmeal2, "to", endmeal2 
	#iterate
	if bias == 'a':
		iterateA(endmeal2, end)
	if bias == 'b':
		iterateB(endmeal2, end)

if totalMin >= 900:
	print "AEA guidelines do not permit rehearsals to run that long."





