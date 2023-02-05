


#step -1
#pip install googletrans==3.1.0a0

#step -2
#Three function 
#1 - listen function
#2 - english translation
#3 - connect

import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator

#1 - listen 

def Listen():

    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) #Listening mode stock problem fixed

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)

    except:
        return""
    
    query = str(query).lower()
    return query

print(Listen())


