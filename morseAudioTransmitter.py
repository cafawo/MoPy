#!/usr/bin/python

# created under Python 2.7

# the sound output works only on a Windows system
import winsound
import time

# morse code dictionary
morseCode = {
			'A': '.-',     'B': '-...',   'C': '-.-.', 
			'D': '-..',    'E': '.',      'F': '..-.',
			'G': '--.',    'H': '....',   'I': '..',
			'J': '.---',   'K': '-.-',    'L': '.-..',
			'M': '--',     'N': '-.',     'O': '---',
			'P': '.--.',   'Q': '--.-',   'R': '.-.',
			'S': '...',    'T': '-',      'U': '..-',
			'V': '...-',   'W': '.--',    'X': '-..-',
			'Y': '-.--',   'Z': '--..',
			'0': '-----',  '1': '.----',  '2': '..---',
			'3': '...--',  '4': '....-',  '5': '.....',
			'6': '-....',  '7': '--...',  '8': '---..',
			'9': '----.',
			}
#print chr(250)*3 + '-'*3 + chr(250)*3  # chr(250) is more pretty than '.'
			
# this function will output a list of words in morse code
def textencoder(textinput):
	words = textinput.split()
	encoded = []
	for w in words:
		characters = list(w)
		morse = [morseCode[c.upper()] if c.upper() in morseCode.keys() else 'E' for c in characters]
		encoded.append(' '.join(morse))
	return(encoded)

# this function provides audio output for a list of words in morse code
def soundtransmitter(morsecode):
	for w in morsecode:
		characters = list(w)
		for c in characters:
			if c == '-':
				winsound.Beep(800, 400) # frequency, duration
				time.sleep(0.2)
			elif c == '.':
				winsound.Beep(800, 200)
				time.sleep(0.2)
			elif c == ' ':
				time.sleep(0.4)
		time.sleep(.6)
	
if __name__ == "__main__":
	print '*'*67
	print 'WELCOME, I will translate your text into a morse code audio signal.'
	print '*'*67

	print '\nYou can type your text and press ENTER, use ctrl+c to quit.\n'

	while True:
		currenttext = raw_input("Text: ")
		morsecode = textencoder(currenttext)
		print(morsecode)
		soundtransmitter(morsecode)
