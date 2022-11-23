import speech_recognition as sr
from selenium import webdriver
from pyttsx3 import speak
import subprocess
import wolframalpha
import ctypes
from urllib.request import urlopen
import win32com.client as wincl
import json
import pyjokes
from time import ctime
import time
import webbrowser as wb
import bs4
import requests
import os
import wikipedia
# CUSTOM MODULES
import whatsapp
import weather
import play
import read
import sendmail
import open
#import

def respond(AudioString):
    speak(AudioString)


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        audio = r.listen(source)
    cmd = ""
    try:
        cmd = r.recognize_google(audio)
        return cmd
    except sr.UnknownValueError:
        respond("did not understand audio")
    except sr.RequestError as e:
        respond("Request Failed; {0}".format(e))
    return cmd


def digital_assistant(data):
    global sub
            
    if 'shutdown' in data:
        os.system('shutdown -s')
    if 'restart' in data:
        os.system('shutdown /r /t 1')
    if 'sleep' in data:
        os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
        
    if 'open github' in data:
        wb.open("https://www.github.com")
        speak("opening github")

    if 'open facebook' in data:
        wb.open("https://www.facebook.com")
        speak("opening facebook")

    if 'open instagram' in data:
        wb.open("https://www.instagram.com")
        speak("opening instagram")   

    if 'open google' in data:
        wb.open("google.com")
        speak("opening google")

    if 'open stackoverflow' in data:
        wb.open("stackoverflow.com")
        speak("opening stackoverflow")

    if 'open yahoo' in data:
        wb.open("https://www.yahoo.com")
        speak("opening yahoo")
            
    if 'open gmail' in data:
        wb.open("https://mail.google.com")
        speak("opening google mail") 
            
    if 'open snapdeal' in data:
        wb.open("https://www.snapdeal.com") 
        speak("opening snapdeal")  
            
    if 'open amazon' in data or 'shop online' in data:
        wb.open("https://www.amazon.com")
        speak("opening amazon")

    if 'open flipkart' in data:
        wb.open("https://www.flipkart.com")
        speak("opening flipkart")

    if 'open youtube' in data:
        wb.open("www.youtube.com")
        speak("opening youtube")
                    
    if 'open app' in data:
        name = data.split(" ")
        app_name = " ".join(name[2:])
        on_app = open.open(app_name)
        speak(app_name)
        
    if 'applist' in data:
        open.applist()    
        
    if "how are you" in data:
        speak("I am well")

    if "what time is it" in data:
        speak(ctime())

    if "stop listening" in data or "stop" in data or "quit" in data:
        lis = False
        print('Listening stopped')
        return lis

    if ("WhatsApp" or "whatsapp" or "WHATSAPP") in data:
        whatsapp.askinfo()
        # whatsapp.whatsapp_send(user, message)

    if "what can you do" in data:
        respond("can handle pretty much all your stuff, sir! however i am still learning so i'll be able to perform "
                "more task in future")

    if "where is" in data or "navigate to" in data:
        l = data.split(" ")
        loc = " ".join(l[2:])
        location_url = f"https://www.google.com/maps/place/{str(loc)}"
        respond("Hold on Ayush, I will show you where " + loc + " is.")
        browser = webdriver.Chrome()
        browser.get(location_url)
        time.sleep(1)
        search = browser.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div["  # type: ignore
                                               "1]/button")
        search.click()
        time.sleep(3)
    
    if ("weather" or "climate") in data:
        weather.info(data)
    
    if 'joke' in data:
            speak(pyjokes.get_joke())
    
    if "calculate" in data:
             
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = data.lower().split().index('calculate')
            query = data.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
            
    if "want to watch" in data or "stream" in data:  # i want to watch tanmay bhat on youtube
        l = data.split(" ")
        iofp = l.index("on")
        if "stream" in data:
            video = "+".join(l[2:iofp])
        else:
            video = "+".join(l[4:iofp])
        platform = " ".join(l[iofp + 1:])
        print(platform)
        play.movies(video, platform)

    if "play" in data:
        l = data.split(" ")
        song = " ".join(l[1:])
        play.music(song)

    if "read" in data or "search" in data or "explain" in data or "what is" in data or "details" in data or "what are" in data:
        l = data.split(" ")
        # i = l.index("about")
        topic = l[-1]
        read.wikipedia(topic)

    if "email" in data:
        print(data)
        l = data.split(" ")
        respond("please enter the email address of the recipient")
        to = input()
        if "regarding" in data:
            r = l.index('regarding')
            sub = l[r + 1]
        else:
            respond("please tell me the subject regarding e-mail")
            sub = listen()
        respond("kindly tell me the body of e-mail")
        body = listen()

        sendmail.send(to, sub, body)
    
    
    if "who are you" in data or "about you" in data or "your details" in data:
            who_are_you = "I am juhi an A I based computer program but i can help you lot like a your assistant ! try me to give simple command !"
            print(who_are_you)
            speak(who_are_you)

    if 'who make you' in data or 'who made you' in data or 'who created you' in data or 'who develop you' in data:
            speak(" For your information juhi Created me !    I can show you his Linked In profile if you want to see.    Yes or no .....")
            ans_from_user_who_made_you = listen()
            if 'yes' in ans_from_user_who_made_you or 'ok' in ans_from_user_who_made_you or 'yeah' in ans_from_user_who_made_you:
                wb.open("https://www.linkedin.com/in/ayush-kumar-namdeo")
                speak('opening his profile...... please wait')
    print(data)
    
    if 'news' in data:
             
            try:
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))
 
         
    if 'lock window' in data:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
                
    lis: bool = True
    return lis

if __name__ == "__main__":
    speak("Hello. what can i do for you?")
    # time.sleep(1)
    listening = True
    while listening:
        task = listen()
        listening = digital_assistant(task)