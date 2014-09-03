#!/usr/bin/python

# Decimal to Hexidecimal converter
# author: Kiri Strack-Grose
# Aug 3, 2014

#get the number
orig = int(raw_input("What decimal number would you like to convert to hexidecimal? "))
rem = ""
#define the functions
def converter(numb):
	if numb == 10:
		return 'A'
	elif numb == 11:
		return 'B'
	elif numb == 12:
		return 'C'
	elif numb == 13:
		return 'D'
	elif numb == 14:
		return 'E'
	elif numb == 15:
		return 'F'
	elif numb == 16: 
		return '0'
	elif numb > 16:
		return "youfuckedup"
	else:
		return str(numb)

#do eeet
while orig >= 16:
	mod = orig%16
	conv = converter(mod)
	rem = str(conv)+rem
	orig = orig/16

#and the first digit
if orig < 16:
	rem = str(converter(orig))+rem

print "In hexidecimal, that is " + rem