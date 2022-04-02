# Used camelCase notation...

import os               # built-in module
import webbrowser       # built-in module
import datetime         # built-in module
# import random           # built-in module

import pywhatkit                    # pip install pywhatkit
import wikipedia                    # pip install wikipedia
import pyttsx3                      # pip install pyttsx3
from googlesearch import search     # pip install google
import speech_recognition as sr     # pip install speechRecognition

# also install "PyAudio" module, else speech_recognition will not work..
# pip install pyaudio

# setting the voice... index "0" for male and "1" for female
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# neccessary functions "speak", and "takeCommand"
def speak(audio):
    '''
    *This function takes a string as an input and speaks that input...
    *Works offline
    '''
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    # It takes microphone input from the user and returns string output
    '''
    *This works online...Needs internet without internet it will not work
    *This function listens what we speak and returns a string using "google" server ...
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        print("Say that again please...")
        return "None"  # None string will be returned
    return query

# Additional features

def wishMe():
    '''
    *This function wishes according to time...
    *This wished total 3 : Good Morining, Good Afternoon and Good Evening....
    '''
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Flash Sir. Please tell me how may I help you.")


def searchWiki(search):
    speak('Searching Wikipedia...Please wait Sir...')
    search = search.replace("wikipedia", "")
    print(f"qurey : {search}")
    results = wikipedia.summary(search, sentences=2)
    speak("According to Wikipedia")
    # print(results)
    speak(results)
    exit()

def openYoutube():
    speak("Opening Youtube Sir...")
    webbrowser.open('youtube.com')
    exit()

def openGoogle():
    speak("Opening Google sir...Please Wait..")
    webbrowser.open("google.com")

# def playMusic():
#     music_dir = "D:\\songs\\hindi_songs"
#     songs = os.listdir(music_dir)
#     # print(songs)
#     os.startfile(os.path.join(music_dir, random.choice(songs)))
#     exit()

def tellTime():
    strTime = datetime.datetime.now().strftime("%I:%M:%S")
    speak(f"The time is {strTime}")
    exit()

def openVsCode():
    codePath = "C:\\Users\\91628\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)
    exit()

def searchGoogle(question):
    print("query recieved...")
    if 'search google' in question:
        question = question.replace("search google", "")
        print(f"the question was : {question}")

    elif 'google' in question:
        question = question.replace("google", "")

    elif 'search in google' in question:
        question = question.replace("search in google", "")
    for i in search(question, tld="co.in", num=10, stop=3, pause=2):
        print(i)

def playOnYt(song):
    song = song.replace("play", "")
    print(song)
    pywhatkit.playonyt(song)


# main
if __name__ == "__main__":
    # speak("Hello Mr.Harsh, I am your robot")
    
    wishMe()

    while True:

    # query = input("enter text to check : ")
    # searchGoogle(query)

    query = takeCommand().lower()
    # query = 'open google'.lower()
    # Logic for executing tasks based on query
    if 'wikipedia' in query:
        searchWiki(query)
    elif 'open youtube' in query:
        openYoutube()
    elif 'open google' in query:
        openGoogle()
    elif 'what is the time' in query or 'tell me the time' in query or 'tell me the current time' in query:
        tellTime()
    elif 'exit' in query:
        speak("Exiting the program sir")
        exit()
    elif 'open code' in query or 'open vs code' in query or 'open visual studio code' in query:
        openVsCode()
    elif 'google' in query or 'search google' in query:
        print("came to google execute section")
        searchGoogle(query)
    # elif 'play music' in query or 'play song' in query:
    #     playMusic()

    elif 'play' in query:
        playOnYt(query)
    else:
        speak("Please tell something do Sir...")
