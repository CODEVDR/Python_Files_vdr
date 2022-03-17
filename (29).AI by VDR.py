import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os




engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishing():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")



    speak("This VDR . How may i help you sir!!!!")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING !!!!")
        r.pause_threshold = 10
        audio = r.listen(source)
    try:
        print("RECOGNISING !!!!")
        query =r.recognize_google(audio, language="en.in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please......")
        return "None" 
    return query


if __name__ == "__main__":
   wishing()
   if 10:
       query = takeCommand().lower()
       if "wikipedia" in query:
            speak("Searching in Wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("Acording to Wikipedia")
            print(results)
            speak(results)
        
       elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube")
       elif 'open google' in query:
           webbrowser.open("google.com")
           speak("opening google")
       elif 'open whatsapp' in query:
           webbrowser.open("web.whatsapp.com")
           speak("opening whatsapp")
       elif 'open facebook' in query:
           webbrowser.open("facebook.com")
           speak("opening facebook")
       elif "play music " in query:  
           music="E:\\RELAX"
           songs=os.listdir(music)
           print(songs)
           os.startfile(os.path.join(music,songs[0]))

       elif "time" in query:
           strTime=datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"Sir , the time is {strTime}")
       elif "my name" in query:
           speak("vdr")
       elif "baby" in query:
           speak("Playing baby-justin biber")
           webbrowser.open("https://youtu.be/kffacxfA7G4?list=RDMMG0Hx6uN2AJE")
           
