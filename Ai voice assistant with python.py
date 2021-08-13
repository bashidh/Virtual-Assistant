import pyttsx3       #text to speech 
import datetime
import speech_recognition as sr   #pip install SpeechRecognition
import pyaudio    # pip install pipwin /n pipwin install pyaudio
import wikipedia
import os
import webbrowser
import subprocess
import smtplib
import pyjokes #pip install pyjokes
import speedtest #pip install speedtest

engine=pyttsx3.init() #initialize all pyttsx3 modules
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speech(audio):
    engine.say(audio)
    engine.runAndWait()   #speech audible to you

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    day=int(datetime.datetime.now().day)
    speech("hi sir the date is")
    print("{}/{}/{}".format(day,month,year))
    speech(day)
    speech(month)
    speech(year)

def time():
    time=datetime.datetime.now().strftime('%I:%M:%S')
    speech("hi sir the  time is")
    print("{}".format(time))
    speech(time)

def joke():
    j=pyjokes.get_joke()
    print(j)
    speech(j)
    

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your emailid', 'password')
    server.sendmail('your emailid', to, content) #before turn on lesssecure apps in google https://myaccount.google.com/u/1/lesssecureapps?pli=1&pageId=none
    server.close()


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speech("good morning sir")
        speech(" how can i help you")
    elif hour>=6 and hour<12:
        speech(" how can i help you")
        speech("good night sir")
    elif hour>=6 and hour<12:
        speech("good evening sir")
        speech(" how can i help you")
    else:
        speech("good night sir")
        speech("I am your Assistant")
        speech("how can i help you")


def takeusercommand():
    r=sr.Recognizer()      #spoken words to text
    with sr.Microphone() as source:
        speech("listening.....")
        print("Listening......")
        r.pause_threshold=0.5   #pause for 1 sec
        audio=r.listen(source)

    try:
        print("Recognizing......")
        query=r.recognize_google(audio,language='en-in')  #convert pronounced audio into text 
        print(query)
       
    except Exception as e:
        print(e)
        speech("Sorry unable to hear your voice...")
        return "None"

    return query
        
if __name__=="__main__":
    clear = lambda: os.system('cls')
    clear()
    #wishme()
    while(True):
        query=takeusercommand().lower()
        if "time" in query:
            time()
        if "date" in query:
            date()
        if 'wikipedia' in query:
            speech('Searching.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speech("According to Wikipedia.....")
            print(results)
            speech(results)
        if "send mail"  in query:
            try:
                speech("whom should i send the mail?")
                to=input()
                speech("what should i say?")
                content=takeusercommand()
                sendemail(to,content)
                speech("email has been sent successfully")
            except Exception as e:
                print(e)
                speech("sorry not able to sent the mail")

        if "open youtube" in query:
            speech("opening.....")
            webbrowser.open("youtube.com")

        if "shutdown" in query:
            speech("do you want to shutdown")
            shutdown=input("Type yes/no : ")
            if shutdown=="yes":
                os.system("shutdown /s /t 1")
            else:
                exit()

        if "open google" in query:
            speech("opening.....")
            webbrowser.open("google.com")
         
        if "remember" in query:
            speech("what should i remember")
            data=takeusercommand()
            speech("you said me to remember"+data)
            year=int(datetime.datetime.now().year)
            month=int(datetime.datetime.now().month)
            day=int(datetime.datetime.now().day)
            remember=open("rem.txt","w")
            remember.write("{}/{}/{} : ".format(day,month,year))
            remember.write(data)
            remember.close()
        
        if "do you know anything" in query:
            remember=open("rem.txt","r")
            print(remember.read())
            speech("you said me to remember"+ remember.read())

        if "joke" in query:
            joke()
       
        if "offline" or "exit" in query:
            quit()
