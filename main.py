#!/usr/bin/env python
#coding:utf8
# Author by: Musa Sakizci 2017 
from gtts import gTTS
from wordlist import words


def Main():
    x = -1
    while(x<60):
        x +=1
        word = words[x]
        print word    
        tts = gTTS(text = word, lang = "tr" )  
        tts.save("voice/"+word+".wav")       
       
Main()
