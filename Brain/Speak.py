import pyttsx3
from playsound import playsound
playsound("C:\\Users\\B75GAMER\\Documents\\Maya Voice\\intro.mp3")
def Speak(Text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[2].id)
    engine.setProperty('rate',190)
    print("")
    print(f"You : {Text}.")
    print("")
    engine.say(Text)
    engine.runAndWait()
Speak("iam process your voice command.")
Speak("My name is maya")
Speak("How can i help you?")