  
import pyttsx3
import datetime as dt
import speech_recognition as sr
import wikipedia
import webbrowser
import string
import os
from translate import Translator



engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty("voice",voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    time=int(dt.datetime.now().hour)
    if time>=0 and time<12:
        speak("Hello ! ,Good Morning!")
    elif time>=12 and time<16:
        speak("Hello ! Good afternoon!")
    elif(time>=16 and time<=21):
        speak("Hello ! Good evening!")
    
    speak("I am Zira , How may I help you ?")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold=3500
        r.pause_threshold=0.8
        audio=r.listen(source)
    try:
        print('Recognizing...')
        query=r.recognize_google(audio,language="en")
        print(f"User Said: {query}\n")
    
    except Exception as e:
        print("Say that again")
        return "None"
    return query


if __name__ == "__main__":
    
    wishMe()
    # Logic for executing task 
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query=query.replace("wikipedia"," ")
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com/")
        
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.co.in/")
        
        elif 'open stack overflow' in query:
            speak("Opening Stackoverflow")
            webbrowser.open('https://stackoverflow.com/')
        
        elif 'play music' in query:
            music_dir='D:\\Music'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'time' in query:
            time_now=dt.datetime.now().strftime("%H:%M:%S")
            speak(time_now)
        
        elif 'code' in query:
            code_path="C:\\Users\\Gudipalli Tarun\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening code")
            os.startfile(code_path)
        
        elif 'spotify' in query:
            spotify_path="C:\\Users\\Gudipalli Tarun\\AppData\\Roaming\\Spotify\\Spotify.exe"
            speak("Opening Spotify")
            os.startfile(spotify_path)
        elif 'chrome' in query:
            chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_path)
        
        elif 'translator' in query:
            speak("The available languages are German , Italian , French , Hindi")
            r1=sr.Recognizer()
            with sr.Microphone() as source2:
                print("Choose the language...")
                # speak("Choose the language")
                r1.energy_threshold=3500
                r1.pause_threshold=0.8
                audio1=r1.listen(source2)
            try:
                print('Recognizing language...')
                say=r1.recognize_google(audio1,language="en")
                print(f"You spoke: {say}\n")

                if "German" in say:
                    speak("Say something to translate in German")
                    r3=sr.Recognizer()
                    with sr.Microphone() as source3:
                        print("Listening to translate in to German...")
                        r3.energy_threshold=3500
                        r3.pause_threshold=0.8
                        audio3=r3.listen(source3)
                    try:
                        print('Recognizing to translate in to Greman...')
                        say2=r3.recognize_google(audio3,language="en")
                        print(f"User Said: {say2}\n")
                        trans=Translator(to_lang="German")
                        translation=trans.translate(say2)
                        print(translation)
                        speak(translation)
                    except Exception as e:
                        print(e)
                elif "Italian" in say:
                    speak("Say something to translate in Italian")
                    r4=sr.Recognizer()
                    with sr.Microphone() as source4:
                        print("Listening to translate to Italian...")
                        r4.energy_threshold=3500
                        r4.pause_threshold=0.8
                        audio4=r4.listen(source4)
                    try:
                        print('Recognizing to tranaslate in to Italain...')
                        say3=r4.recognize_google(audio4,language="en")
                        print(f"User Said: {say3}\n")
                        trans=Translator(to_lang="Italian")
                        translation=trans.translate(say3)
                        print(translation)
                        speak(translation)
                    except Exception as e:
                        print(e)
                
                elif "French" in say:
                    speak("Say something to translate in French")
                    r5=sr.Recognizer()
                    with sr.Microphone() as source5:
                        print("Listening to translate to French...")
                        r5.energy_threshold=3500
                        r5.pause_threshold=0.8
                        audio5=r5.listen(source5)
                    try:
                        print('Recognizing to tranaslate in to French...')
                        say4=r5.recognize_google(audio5,language="en")
                        print(f"User Said: {say4}\n")
                        trans=Translator(to_lang="French")
                        translation=trans.translate(say4)
                        print(translation)
                        speak(translation)
                    except Exception as e:
                        print(e)
                
                elif "Hindi" in say:
                    speak("Say something to translate in Hindi")
                    r6=sr.Recognizer()
                    with sr.Microphone() as source6:
                        print("Listening to translate to Hindi...")
                        r6.energy_threshold=3500
                        r6.pause_threshold=0.8
                        audio6=r6.listen(source6)
                    try:
                        print('Recognizing to tranaslate in to Hindi...')
                        say5=r6.recognize_google(audio6,language="en")
                        print(f"User Said: {say5}\n")
                        trans=Translator(to_lang="Hindi")
                        translation=trans.translate(say5)
                        print(translation)
                        speak(translation)
                    except Exception as e:
                        print(e)
                
            except Exception as e:
                print(e)
        





    
        
        elif 'exit' in query:
            exit(0)
