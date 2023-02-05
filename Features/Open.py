import os
import keyword
import pyautogui
import webbrowser
from time import sleep
import datetime
from Body.Speak import Speak

def OpenExe(Query):
    Query = str(Query).lower()

    if "visit" in Query:
        Nameofweb = Query.replace("visit ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "launch" in Query:
        Nameofweb = Query.replace("launch ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "open" in Query:
        Nameofweb = Query.replace("open ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True


    
    elif "start" in Query:
        Nameoftheapp = Query.replace("start ","")
        if "chrome" in Nameoftheapp:
         os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
        
        elif "discord" in Nameoftheapp:
         os.startfile(r"C:\Users\B75GAMER\AppData\Local\Discord\app-1.0.9010\Discord.exe")
        
        elif "visual studio code" in Nameoftheapp:
         os.startfile(r"C:\Users\B75GAMER\AppData\Local\Programs\Microsoft VS Code\Code.exe")   
    
        return True

    elif "time" in Query:
        time=datetime.datetime.now().strftime('%I:%M %p')
        Speak(time)
    return True