#!/usr/bin/python

import random

# begin the word list, complete with definitions
DICT = ["oleaginous", "noctivagant", "brontide", "xyloid", "drouk", "febrile", "bergamot", "roscid", "hedomadal", "aubade", "vicissitude", "jannisary", "acrimonious", "meliorism", "scimachy", "antidiluvian", "perspicacious", "optative", "pugnacious", "redamancy"
, "isabelline", "pugnacious", "redamancy", "columbine", "thaumaturgy", "adoxography"]

# and a const variable disclaimer about the definitions
DISCLAIM = "These definitions were found in the Oxford English Dictionary."

# variables          
health = 10                              # number of tries
word = random.choice(DICT)               # the word to be used
progress = "_" * len(word)               # display one space for each letter
used = []                                # letters already guessed

word = "pants" #JUST FOR NOW!!!!!!

print '''You ascend the parlous steps of the gallows. The hangman's
countenance contorts into a macabre mockery of a grin.
His odiferous breath occludes the passage of oxygen into
your lungs, a poisonous miasma of acrimony.  
"Welcome to Hangman," he practically expectorates. "Good. Luck."'''

# a function to display the stats
def display(used, health, progress):
	print "\nThese are the letters you've used: \n", used
	print "Your health is currently: ", health
	print "The word is: \n", progress

display(used, health, progress)


prompt = raw_input("\n Guess a letter: ")   # the guess!


# create a function to check that the guess is a letter and is only one letter
def input(prompt):
	while len(prompt) > 1: # if it's longer than 1 character
		prompt = raw_input("\nGuess only ONE letter: ")
	while prompt.isalnum() and not prompt.isalpha(): # if it's not a letter
		prompt = raw_input("\nGuess a LETTER: ")
	while (guess in used):
		prompt = raw_input("\nGuess a NEW letter: ")
	if (len(prompt) == 1) and (prompt.isalpha() and (prompt not in used)): 
		return prompt

guess = prompt #might wanna take this out later!!!!!
	
# the setup of the game:
while (health > 0) and (display != word): # if you haven't died and haven't won:
	# call the input function
	input(prompt)  #only calling the function

	#if everything is working okay:
	used.append(guess) # add the guess to the used list

	if (guess in word):
		print "\nYou guessed correctly!"
		# add the letter to progress
#HELP I DON'T GET THIS
		new = ""
		for i in range(len(word)):
			if guess == word[i]:
				new += guess
			else:
				new += progress[i]
			progress = new		
		# and display everything??
#okay I'm back to things I understand
	else:
		print "\nSorry, ", guess, "isn't in the word."
		health -= 1
	# call the display function outside the if/else but in the while loop
	display(used, health, progress)
	
# if they die:
if health == 0:
	print '''The hangman leers lecherously as his porcine hands fumble
the scatological noose around your vitreous neck.  He wrenches
the lever and you fall, insensate, to your unconscionable death.'''

# if they win:
if progress == word:
	print "You have won!  The word is, ", word
