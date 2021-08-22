import pyttsx3
import speech_recognition as sr
import wikipedia
import os
import pyjokes
import webbrowser
import datetime
import wolframalpha
import requests
import subprocess
from bs4 import BeautifulSoup as soup



engine = pyttsx3.init("sapi5")
MASTER="human"

voices = engine.getProperty("voices")
print(voices[0].id)
engine.setProperty("voices", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    

    if hour>=0 and hour <12:
        speak("good morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("good afternoon" + MASTER)

    else:
        speak("good Evening" + MASTER)

    speak("i am your assistant. How may I help you?")


def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        #print("i am listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        #print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        #print(f"user said : {query}\n")
        #speak(query)
    except Exception as e:
        #print(e)
        #print("say that again")
        return "None"
    return query


if __name__ == '__main__':
    speak("i am jarvis, build with love by maratha coder ")
    print("ask me anything")
    wishMe()
    while(True):
        query1=takeCommand().lower()
        print("say, hey jarvis")
        
        
        if "jarvis" in query1:
            speak(" yes sir")
            print("listening....")
            query=takeCommand().lower()
            if 'wikipedia' in query:
                speak("searching wikipedia")
                query=query.replace("wikipeda","")
                results = wikipedia.summary(query,sentences=2)
                speak("according to wikipedia")
                speak(results)
                print(results)
            elif 'joke' in query:
                speak(pyjokes.get_joke())


            elif 'open google' in query:

                speak("here you go on google\n")
            
                webbrowser.open("www.google.com")

            elif 'open youtube' in query:
                speak("Here you go to youtube\n")
                webbrowser.open("www.youtube.com")

            elif "log off" in query or "sign out" in query:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])
            
            elif "play music" in query:
                music_dir = "C:\\Users\\91700\\Music\\music"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))
            
            elif "weather" in query:
                api_key="8ef61edcf1c576d65d836254e11ea420"
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                speak("whats the city name")
                city_name=takeCommand()
                complete_url=base_url+"appid="+api_key+"&q="+city_name
                response = requests.get(complete_url)
                x=response.json()
                if x["cod"]!="404":
                    y=x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature in kelvin unit is " +
                        str(current_temperature) +
                        "\n humidity in percentage is " +
                        str(current_humidiy) +
                        "\n description  " +
                        str(weather_description))
                    print(" Temperature in kelvin unit = " +
                        str(current_temperature) +
                        "\n humidity (in percentage) = " +
                        str(current_humidiy) +
                        "\n description = " +
                        str(weather_description))
            else:
                speak("sorry, say that again")