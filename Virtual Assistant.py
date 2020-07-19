import datetime
import os
import smtplib  # for sending  mails
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good morning")
    elif  hour>=12 and hour<18 :
        speak("Good afternoon!")  
    else:
        speak("Good evening")    

    speak("Hi I am Mr. Anand personal virtual assistant, How may I help you ?")    

def takeCommand():
    #It takes audio as input and gives string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #at video 20:50
        audio = r.listen(source)                          

    try:
        print("Recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
        
    except Exception as e:
        # print(e)
        print("Please Repeat.....")
        return "None"
    return query

if __name__ == "__main__":
   wishMe()
   while True:
       query = takeCommand().lower()
       #    logic for task
       if 'wikipedia' in query:
           speak("Searching wikipedia...")
           query = query.replace("wikipedia","")
           results = wikipedia.summary(query,sentences=2)
           print(results)
           speak(results)
       elif 'open youtube' in query:
             webbrowser.open("youtube.com")

       elif 'open google' in query:
             webbrowser.open("google.com")

       elif 'open stackoverflow' in query:
           webbrowser.open("satckoverflow.com")

       elif 'open visual studio' in query:
           codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)

       elif 'spotify' in query:
           spotify = "C:\\Program Files\\WindowsApps\\SpotifyAB.SpotifyMusic_1.132.618.0_x86__zpdnekdrzrea0\\Spotify.exe"  
           os.startfile(spotify)  
       elif 'quit' in query:
           speak("Thank you have a good day")
           exit() 