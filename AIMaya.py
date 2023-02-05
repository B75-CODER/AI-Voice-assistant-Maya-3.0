from Brain.TrainAIBrain import ReplyBrain
from Body.Listen import MicExecution
print(">> Starting The Maya : wait for some seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Starting The Maya : Wait for few second more")
from TrainTask import MainTasksExecutor
from playsound import playsound
import datetime

def MainExecution():
    Speak("Hello sir")
    Speak("I am maya, Iam ready to assist You")
    while True:

        Data = MicExecution()
        Data = str(Data)
        if len(Data)<3:
            pass
        elif "bye bye" in Data:
            Speak("Ok sir Bye sir, You call me Anytime!")
            Speak("Have a good day sir...")
            break
        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

        valueReturn = MainTasksExecutor(Data)
        if valueReturn==True:
            pass

def wakeupDetect():
    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">>Wake up maya Detected!!")
        playsound("C:\\Users\\B75GAMER\\Documents\\Maya Voice\\wakeup activate.wav")
        print("")
        MainExecution()      
    else:
        pass
     
wakeupDetect()