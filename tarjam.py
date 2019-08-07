#!/usr/bin/env python3

from googletrans import Translator
import os 


translator = Translator() 
def translate_the_word(word):
	lang = translator.detect(str(word)).lang
	if lang == 'en' : 

		translatetext=translator.translate(word,dest='ar')
	else : 
		translatetext=translator.translate(word)
	send0nnotify(translatetext.text)


def send0nnotify(word): 
	command = "notify-send 'Translator مطرجم ' '"+word+"'"
	os.system(command)

myCout = os.popen('xclip -o').read()
translate_the_word(myCout)