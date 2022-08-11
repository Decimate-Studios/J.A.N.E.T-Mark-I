import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia

def TakeCommand():

    r = sr.Recognizer

    with sr.Microphone() as source:
        print("listening")

        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("recognizing")

            Query = r.recognize_google(audio, language="en")
            print("the command is printed = ", Query)

        except Exception as e:
            print(e)
            print("say that again sir")
            return "None"

        return Query

def speak(audio):
    engine = pyttsx3.int()
    voices = engine.getProperty("voices")

    engine.setProperty("voice", voices[1].id)

    engine.say(audio)

    engine.runAndWait()

def tellDay():
    day = datetime.datetime.today().weekday() + 1

    day_dict = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

    if day in day_dict.keys():
        day_of_the_week = day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def tellTime():
    time = str(datetime.datetime.now())

    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak(Self, "The time is " + hour + " " + min)

def hello():
    speak("Hello sir. / How may I help you")

def Take_Query():
    hello()

    while(True):

        query = TakeCommand().lower()

        if "open youtube" in query:
            speak("Open youtube")

            webbrowser.open("https://www.youtube.com/")

            continue
        
        elif "open emails" in query:
            speak("Open youtube")

            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

            continue
        elif "what day is it" in query:
            tellDay()
            continue
        elif "what time is it" in query:
            tellTime()
            continue
        elif "from wikipedia" in query:
            speak("Checking wikipedia")
            query = query.replace("from wikipedia", "")
            query = query.replace("get", "")

            result = wikipedia.summary(query, sentences=4)
            speak(result)
        elif "your name" in query:
            speak("My name is, just a networked exponential toolbox, or janet.")
        elif "terminate program" in query:
            speak("Terminating program. Goodbye.")
            exit()
        
if __name__ == '__main__':
    Take_Query()