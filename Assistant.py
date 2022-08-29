import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    
    speak("I am Olivia, Plese tell me how may i help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        r.energy_threshold = 3500
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"user said {query}\n")
    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    takecommand()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('searching in wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'C:\\My Files\\Songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randrange(0,4)]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'be my girlfriend' in query:
            speak("No but i will think about it...")
        
        elif 'you committed' in query:
            speak("yes to my work")

        elif 'go for a date' in query:
            speak("sorry, i don't have time")

        elif 'exit' in query:
            exit()
        