#!/usr/bin/python


#Purpose of Educational Hangman:  to play the classic Hangman game
#but to avoid being bored by all of the ubiquitous, simplistic words

#current bug: I know all of the commented-out words exist
#but I was having trouble finding them on OED online.

#code checked against Michael Dawson's

import random

# begin the word list, complete with definitions
DICT = {"oleaginous":'''a. Having the nature or properties of oil; containing oil or 
an oily substance; oily, fatty, greasy.
b. Producing or yielding oil.
c. Exaggeratedly and distastefully complimentary; obsequious, unctuous.'''
,
"noctivagant":"That wanders or roams about at night.", 
#"brontide", 
#"xyloid", 
"drouk":"To drench (as with heavy rain).", 
"febrile":'''a. Of a person: Affected by, or suffering from, fever.
b. Of or pertaining to fever; produced by or indicative of fever; feverish.'''
 ,
"bergamot":'''A tree of the orange and lemon kind ( Citrus bergamia); 
from the rind of the fruit a fragrant oil is prepared, 
called Essence of Bergamot.'''
 ,
"roscid":"Dewy, moist; falling like dew.", 
#"hedomadal", 
"aubade":"A musical announcement of dawn, a sunrise song or open-air concert.", 
"vicissitude":'''The fact of change or mutation taking place in a particular thing 
or within a certain sphere; the uncertain changing or mutability of something.'''
, 
#"jannisary", 
"acrimonious":'''a. Acrid.
b. Esp. of speech or a debate: bitter and angry in tone or manner; bitter-tempered.'''
, 
"meliorism":'''The doctrine that the world, or society, may be improved and suffering 
alleviated through rightly directed human effort; a policy embodying this doctrine.'''
, 
#"scimachy", 
#"antidiluvian", 
"perspicacious":'''a. Of eyes, sight, etc.: keen, sharp; clear-sighted. Chiefly fig.
b. Of a person, wit, etc.: penetrating; perceptive, discerning.'''
, 
"optative":"Having the function of expressing wish or desire.", 
"pugnacious":"Eager or quick to quarrel or fight; given to fighting or arguing; belligerent, contentious.", 
"isabelline":"Of an Isabella colour, greyish yellow.", 
"redamation":"The action of loving someone in return.", 
"columbine":'''a. Of, belonging to, or of the nature of, a dove or pigeon.
b. Dove-like; resembling the dove as a type of innocence or gentleness. 
c. Of the colour of a pigeon's neck, dove-coloured.'''
, 
"thaumaturgy":"The working of wonders; miracle-working; magic.", 
#"adoxography"
}
#use just the keys for now:
words = DICT.keys()

# and a const variable disclaimer about the definitions
DISCLAIM = "These definitions were found in the Oxford English Dictionary."

# variables          
health = 15                              # number of tries
word = random.choice(words)              # the word to be used
progress = "_" * len(word)               # display one space for each letter
used = []                                # letters already guessed


print '''\n\nYou ascend the parlous steps of the gallows. The hangman's
countenance contorts into a macabre mockery of a grin.
His odiferous breath occludes the passage of oxygen into
your lungs, a poisonous miasma of acrimony.  
"Welcome to Hangman," he practically expectorates. 
"Good. Luck."'''

# a function to display the stats
def display(used, health, progress):
	print "\nThese are the letters you've used: \n", used
	print "Your health is currently: ", health
	print "The word is: \n", progress

display(used, health, progress)

# create a function to check that the guess is a letter and is only one letter
def input():
	guess = raw_input("\n Postulate a letter: ").lower()   # the guess!
	while len(guess) > 1: # if it's longer than 1 character
		print "\n'You schlemiel!'  The hangman gnars into your face.\n'I said, guess only ONE letter!'"
		guess = raw_input("Make another endeavor: ")
	while (guess in used):
		print "\n'You schlemiel!'  The hangman gnars into your face.\n'You must guess NEW letter!'"
		guess = raw_input("Make another endeavor: ")
	while not guess.isalpha():
		print "\n'You schlemiel!'  The hangman gnars into your face.\n'I said, guess a LETTER.'"
		guess = raw_input("Make another endeavor: ")
	if (len(guess) == 1) and (guess.isalpha() and (guess not in used)): 
		return guess

	
# the setup of the game:
while ((health > 0) and (progress != word)): # if you haven't died and haven't won:
	# call the input function
	guess = input()  #only calling the function

	#to change the display:
	if (guess in word):
		print '''\nFrom the flagging of the hangman's visage, you discern
with joyance that your conjecture was accurate!'''
		# add the letter to progress
		new = ""
		for i in range(len(word)):
			if guess == word[i]:
				new += guess
			else:
				new += progress[i]
		progress = new		

	else:
		print "\n\nThe hangman's physiognomy flushes with portentous delectation.\nYou cognize that", guess, "isn't in the word."
		health -= 1

	used.append(guess)	
	# call the display function outside the if/else but in the while loop
	display(used, health, progress)
	
# if they die:
if health == 0:
	print '''\nThe hangman leers lecherously as his porcine hands fumble
the asperous noose around your vitreous neck.  He wrenches
the lever and you fall, insensate, to your unconscionable death.
The last thing you hear before the gloaming in your eyes is complete
is the hangman's parting whisper.'''
	print ""
	print "'The word was", word, "\b.  It means:"
	print DICT[word], "\b'"
	print ""	
	print DISCLAIM

# if they win:
if word == progress:
	print '''\nYour laudable cerebration has procured your freedom!
You hasten away from the mortiferous hangman and his noose,
secure in the knowledge that the word is''', word, "/b."
	print ""
	print "'Do you even know what that means?' The hangman shouts\nback at you, a paltry attempt at a parting blow."
	print "Of course you do.  Of course you know that", word, "means:"
	print DICT[word]
	print ""
	print DISCLAIM
