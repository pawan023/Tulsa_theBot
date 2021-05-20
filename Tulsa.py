import pyttsx3 as tts
import datetime as dt
import speech_recognition as sr
import wikipedia as wiki
import webbrowser as wb
import os
import smtplib as sml
import random 

engine = tts.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetings():
    # getting hour of the day 0-24
    hr = int(dt.datetime.now().hour)
    if hr>=0 and hr<12:
        speak("Good morning senpai")
    elif hr>=12 and hr<16:
        speak("Good afternoon senpai")
    elif hr>=16 and hr<10:
        speak("Good evening senpai")
    else:
        speak("Good night senpai")

    speak("I am Tulsa. Please tell me how may i help you")

def takeCommand():
    # it takes audio input from user and returns string as output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 3500
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print("User said : ",query)
    
    except Exception:
        print(("Could not recognize... Repeat please"))
        return "None"
        
    return query

def sendEmail(to,content):
    server = sml.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    # senders mail
    server.login('senders mail','password')
    server.sendmail('senders mail',to,content)
    server.close()

# Driver code
if __name__ == "__main__":

    greetings()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            wikiResult = wiki.summary(query, sentences=3)
            speak("Acoording to wikipedia")
            print(wikiResult)
            speak(wikiResult)
        
        elif 'youtube' in query:
            wb.open("youtube.com")

        elif 'movie' in query:
            movieDir = 'E:\\Movies\\animated'
            movies = os.listdir(movieDir)
            os.startfile(os.path.join(movieDir,random.choice(movies)))

        elif 'time' in query:
            t = dt.datetime.now().strftime("%H:%M:%S")
            speak(f"The time right now is {t}")
            print(t)

        elif 'open code' in query:
            path = "C:\\Users\\pawan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'mail' in query:
            try:
                speak("What message should i send")
                content = takeCommand()
                # receiver mail
                to = "rahul436@gmail.com"
                sendEmail(to,content)
                speak("Email has been send")
            except Exception:
                speak("Sorry, some error occured")
        
        elif 'exit' in query:
            exit()
        
        else:
            pass
