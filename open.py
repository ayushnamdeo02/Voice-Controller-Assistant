import os
import pyttsx3
# pip install AppOpener
from AppOpener import run
def open(name):
        name1=str(name)
        run(name1)
        pyttsx3.speak("opening"+ name)
def applist():
    open("ls")