import pyttsx3
import speech_recognition as sr
import wikipedia
engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")
print(voices[0].id)
engine.setProperty("voices", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    speak("mahika here, how may i assit you")

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
    speak("i am queen mihika build with love by rohan ")
    wishMe()
    while(True):
        query1=takeCommand().lower()
        print("say, hey mahika")
        
        
        if "mahika" in query1:
            speak(" bolo bhos di ke rohan")
            print("listening....")
            query=takeCommand().lower()
            

            if 'wikipedia' in query:
                speak("searching wikipedia")
                query=query.replace("wikipeda","")
                results = wikipedia.summary(query,sentences=2)
                speak("according to wikipedia")
                speak(results)
                print(results)
        