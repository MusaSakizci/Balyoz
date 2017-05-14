#!/usr/bin/env python
#coding:utf8
# Autor by: Musa Sakizci 2017 
from gtts import gTTS
from wordlist import words


def Main():
    x = -1
    while(x<5):
        x +=1
        word = words[x]
        print word    
        tts = gTTS(text = word, lang = "tr" )  
        tts.save("voice/"+word+".wav")       
       
Main()
