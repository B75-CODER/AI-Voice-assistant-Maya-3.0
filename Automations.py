import pywhatkit
from pywikihow import WikiHow , search_wikihow
import webbrowser as web
from Body.Speak import Speak

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term

    web.open(result)
    Speak("This is what i found for your search")
    pywhatkit.playonyt(term)
    Speak("This May Also Help your sir")

    