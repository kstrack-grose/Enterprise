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
#the while loop in AorB() is glitching

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

def AorB():
	print "\nIn general, would you prefer to break \na) 5 minutes every 55 minutes \nor \nb) 10 minutes every 80 minutes? \n"
	bias = raw_input("a or b: ").lower()
#	while bias != "a" and bias != "b":
#		bias = raw_input("Try again. a or b: ").lower
# 	^^ is currently not working for some unknown reason
	return bias

	#how to divide between meal breaks
def timeToChunkA(begin, stop):
	partialDelta = stop - begin
	partialMin = partialDelta.total_seconds()/60
	partialHours = partialMin/60
	intHours = int(partialHours//1)
	#and return intHours, so I can use it in the range
	return intHours

def timeToChunkB(begin, stop):
	partialDelta = stop - begin
	partialMin = partialDelta.total_seconds()/60
	partialChunks = partialMin/90
	intChunks = int(partialChunks//1)
	#return intChunks (they're 90 minutes, not hours) to use in range
	return intChunks

		
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

print "\nPlease enter the rehearsal end time:"
	#datetime for end:
end = datetime(now.year, now.month, day(), hour(), minute())             

#confirm start/end times with user:
print "\nPlease confirm your rehearsal's start time:"
print start
startChoice = raw_input("Was that correct?  Yes or no: ")                
if startChoice.lower()[0] != "y":
 	print "\nPlease enter your start time again. \n"
	start =  datetime(now.year, now.month, day(), hour(), minute()) 
#^basically start from beginning of start inputs


print "\nPlease confirm your rehearsal's end time:"
print end
endChoice = raw_input("Was that correct?  Yes or no: ")                
if endChoice.lower()[0] != "y":
	print "\nPlease enter your end time again. \n"
	end = datetime(now.year, now.month, day(), hour(), minute()) 
#^basically start from beginning of end inputs

bias = AorB()

#more variables:
totalDelta = end - start
totalMin = totalDelta.total_seconds()/60
totalHours = totalMin/60
intHours = int(totalHours//1)
times.append("")
times.append(["Start of rehearsal is", start.strftime('%d, %r')])

#note: WHEN YOU MADE TIMETOCHUNK A FUNCTION, YOU REMOVED NOWTIME FROM IT. DO THAT INDIVIDUALLY.

#NOW BEGINS THE THREE OPTIONS BY MEAL BREAK
#first one: if rehearsal <= 5 hours

if totalMin < 300:
	begin = start
	stop = end
	if bias == 'a':
	        for x in range(0, timeToChunkA(begin, stop)):
		        times.append("")
               		begin = begin + arun
                	times.append(["Start of break is", begin.strftime('%d, %r')])
                	begin = begin + abreak
                	times.append(["End of break is", begin.strftime('%d, %r')])
			#^^adds beginnings and ends of breaks to a list to print out later
	if bias == 'b':
                for x in range(0, timeToChunkB(begin, stop)):
                        times.append("")
                        begin = begin + brun
                        times.append(["Start of break is", begin.strftime('%d, %r')])
                        begin = begin + bbreak
                        times.append(["End of break is", begin.strftime('%d, %r')])
			#^^ditto last comment

if (300 <= totalMin) and (totalMin < 600):
	#MEAL
	halfway = (end - start)/2 + start
	startmeal = halfway - timedelta(0, 0, 0, 0, 30)
	endmeal = halfway + timedelta(0, 0, 0, 0, 30)
	#set variables:
	begin = start
	stop = startmeal
	#aaand call iterate functions for before meal
	if bias == 'a':
                for x in range(0, timeToChunkA(begin, stop)):
                        times.append("")
                        begin = begin + arun
                        times.append(["Start of break is", begin.strftime('%d, %r')])
                        begin = begin + abreak
                        times.append(["End of break is", begin.strftime('%d, %r')])
                        #^^adds beginnings and ends of breaks to a list to print out later
	if bias == 'b':
                for x in range(0, timeToChunkB(begin, stop)):
                        times.append("")
                        begin = begin + brun
                        times.append(["Start of break is", begin.strftime('%d, %r')])
                        begin = begin + bbreak
                        times.append(["End of break is", begin.strftime('%d, %r')])
                        #^^ditto last comment
	times.append("")
	times.append(["Start of meal break is", startmeal.strftime('%d, %r')])
	times.append(["End of meal break is", endmeal.strftime('%d, %r')])
	#reset variables
	begin = endmeal
	stop = end
	#iterate
	if bias == 'a':
                for x in range(0, timeToChunkA(begin, stop)):
                        times.append("")
                        begin = begin + arun
                        times.append(["Start of break is", begin.strftime('%d, %r')])
                        begin = begin + abreak
                        times.append(["End of break is", begin.strftime('%d, %r')])
                        #^^adds beginnings and ends of breaks to a list to print out later
	if bias == 'b':
                for x in range(0, timeToChunkB(begin, stop)):
                        times.append("")
                        begin = begin + brun
                        times.append(["Start of break is", begin.strftime('%d, %r')])
                        begin = begin + bbreak
                        times.append(["End of break is", begin.strftime('%d, %r')])
                        #^^ditto last comment


if (600 <= totalMin) and (totalMin < 900):
	#TWO MEALS
	third = (end - start)/3 + start
	startmeal1 = third - timedelta(0, 0, 0, 0, 30)
	endmeal1 = third + timedelta(0, 0, 0, 0, 30)
	#set variables
	begin = start
	stop = startmeal1
	#iterate
	if bias == 'a':
                for x in range(0, timeToChunkA(begin, stop)):
                        times.append("")
                        begin = begin + arun
                        times.append(["Start of break is", begin.strftime('%d, %r')])
                        begin = begin + abreak
                        times.append(["End of break is", begin.strftime('%d, %r')])
                        #^^adds beginnings and ends of breaks to a list to print out later
	if bias == 'b':
                for x in range(0, timeToChunkB(begin, stop)):
                        times.append("")
                        begin = begin + brun
                        times.append(["Start of break is", begin.strftime('%d, %r')])
                        begin = begin + bbreak
                        times.append(["End of break is", begin.strftime('%d, %r')])
                        #^^ditto last comment
	#mealbreak!
        times.append("")
        times.append(["Start of meal break is", startmeal1.strftime('%d, %r')])
        times.append(["End of meal break is", endmeal1.strftime('%d, %r')])
	#now, calculate second meal
	secondThird = (2*(end-start))/3 + start
	startmeal2 = secondThird - timedelta(0, 0, 0, 0, 30)
	endmeal2 = secondThird + timedelta(0, 0, 0, 0, 30)
	#and reset variables
	begin = endmeal1
	stop = startmeal2
	#iterate
	if bias == 'a':
                for x in range(0, timeToChunkA(begin, stop)):
                        times.append("")
                        begin = begin + arun
                        times.append(["Start of break is", begin.strftime('%d, %r')])
                        begin = begin + abreak
                        times.append(["End of break is", begin.strftime('%d, %r')])
                        #^^adds beginnings and ends of breaks to a list to print out later
	if bias == 'b':
                for x in range(0, timeToChunkB(begin, stop)):
                        times.append("")
                        begin = begin + brun
                        times.append(["Start of break is", begin.strftime('%d, %r')])
                        begin = begin + bbreak
                        times.append(["End of break is", begin.strftime('%d, %r')])
	#mealbreak!
        times.append("")
        times.append(["Start of meal break is", startmeal2.strftime('%d, %r')])
        times.append(["End of meal break is", endmeal2.strftime('%d, %r')])
	#reset variables
	begin = endmeal2
	stop = end
	#iterate
	if bias == 'a':
                for x in range(0, timeToChunkA(begin, stop)):
                        times.append("")
                        begin = begin + arun
                        times.append(["Start of break is", begin.strftime('%d, %r')])
                        begin = begin + abreak
                        times.append(["End of break is", begin.strftime('%d, %r')])
                        #^^adds beginnings and ends of breaks to a list to print out later
	if bias == 'b':
                for x in range(0, timeToChunkB(begin, stop)):
                        times.append("")
                        begin = begin + brun
                        times.append(["Start of break is", begin.strftime('%d, %r')])
                        begin = begin + bbreak
                        times.append(["End of break is", begin.strftime('%d, %r')])


if totalMin >= 900:
	print "AEA guidelines do not permit rehearsals to run that long."


	#CONCLUSION
#add rehearsal end time to list
times.append("")
times.append(["End of rehearsal is", end.strftime('%d, %r')])
#print out the entire list!
for y in range(0, len(times)):
	print times[y]
print "Thank you for using Schedules. Have a good rehearsal!"


