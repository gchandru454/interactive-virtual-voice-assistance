import subprocess
import json
import random
import operator
import datetime
import pyaudio
import pyttsx3
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import speech_recognition as sr
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import sys

import wolframalpha
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jjgui import Ui_jjgui



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = ("I am JJ Assistant")
    print(assname)



def username():
    uname = "Welcome External"
    speak(uname)
    columns = shutil.get_terminal_size().columns

    speak("How can i Help you, Sir")

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()


    def takeCommand(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:

            print("Listening...")
            speak("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, phrase_time_limit=5)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            return "None"

        return query


    def TaskExecution(self):
        wish()
        username()

        while True:
            self.query = self.takeCommand().lower()
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in self.query:
                speak("Here you go to Youtube\n")
                webbrowser.open("youtube.com")

            elif 'open google' in self.query:
                speak("Here you go to Google\n")
                webbrowser.open("google.com")

            elif 'open stackoverflow' in self.query:
                speak("Here you go to Stack Over flow.Happy coding")
                webbrowser.open("stackoverflow.com")

            elif 'play movie' in self.query:
                speak("Here you go with movie")
                # music_dir = "G:\\Song"
                music_dir = "C:\\Users\\GAURAV\\Music"
                songs = os.listdir(music_dir)
                print(songs)
                random = os.startfile(os.path.join(music_dir, songs[1]))

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M")
                print(strTime)
                speak(f"Sir, the time is {strTime}")

            elif 'open opera' in self.query:
                codePath = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(codePath)

            elif 'how are you' in self.query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")

            elif 'fine' in query or "good" in self.query:
                speak("It's good to know that your fine")

            elif "change my name to" in self.query:
                query = query.replace("change my name to", "")
                assname = query

            elif "change name" in self.query:
                speak("What would you like to call me, Sir ")
                assname = takeCommand(self)
                speak("Thanks for naming me")

            elif "what's your name" in self.query or "What is your name" in query:
                speak("My friends call me")
                speak(assname)
                print("My friends call me", assname)

            elif 'exit' in self.query:
                speak("Thanks for giving me your time")
                exit()


            elif 'joke' in self.query:
                print(pyjokes.get_joke("en"))
                speak(pyjokes.get_joke())

            elif "calculate" in self.query:

                app_id = "K27AE5-P642A7TYKA"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)

            elif 'search' in self.query or 'play' in self.query:

                query = query.replace("search", "")
                query = query.replace("play", "")
                webbrowser.open(query)

            elif "who i am" in self.query:
                speak("If you talk then definitely your human.")

            elif "why you came to world" in self.query:
                speak("Thanks to jai. further It's a secret")


            elif 'is love' in self.query:
                speak("It is 7th sense that destroy all other senses")

            elif "who are you" in self.query:
                speak("I am your virtual assistant created by Gaurav")

            elif 'reason for you' in self.query:
                speak("I was created as a Minor project by Mister Gaurav ")

            elif 'change background' in self.query:
                ctypes.windll.user32.SystemParametersInfoW(20,
                                                           0,
                                                           "Location of wallpaper",
                                                           0)
                speak("Background changed successfully")


            elif 'news' in self.query:

                try:
                    jsonObj = urlopen(
                        '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =41a945c1e2d941f5bbc784e950e1b9f7\\times of India 41a945c1e2d941f5bbc784e950e1b9f7\\''')
                    data = json.load(jsonObj)
                    i = 1

                    speak('here are some top news from the times of india')
                    print('''=============== TIMES OF INDIA ============''' + '\n')

                    for item in data['articles']:
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        speak(str(i) + '. ' + item['title'] + '\n')
                        i += 1
                except Exception as e:

                    print(str(e))


            elif 'lock window' in self.query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            elif 'shutdown system' in self.query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

            elif 'empty recycle bin' in self.query:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                speak("Recycle Bin Recycled")

            elif "don't listen" in self.query or "stop listening" in self.query:
                speak("for how much time you want to stop jarvis from listening commands")
                a = int(takeCommand(self))
                time.sleep(a)
                print(a)

            elif "where is" in self.query:
                self.query = self.query.replace("where is", "")
                location = self.query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.nl / maps / place/" + location + "")

            elif "camera" in self.query or "take a photo" in self.query:
                ec.capture(0, "Jarvis Camera ", "img.jpg")

            elif "restart" in self.query:
                subprocess.call(["shutdown", "/r"])

            elif "hibernate" in self.query or "sleep" in self.query:
                speak("Hibernating")
                subprocess.call("shutdown / h")

            elif "log off" in self.query or "sign out" in self.query:
                speak("Make sure all the application are closed before sign-out")
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])

            elif "write a note" in self.query:
                speak("What should i write, sir")
                note = takeCommand(self)
                file = open('jarvis.txt', 'w')
                speak("Sir, Should i include date and time")
                snfm = takeCommand(self)
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)

            elif "show note" in self.query:
                speak("Showing Notes")
                file = open("jarvis.txt", "r")
                print(file.read())
                speak(file.read(6))


            elif "jj" in self.query:

                wish()
                speak("JJ in your service Mister")
                speak(assname)

            elif "weather" in self.query:


                api_key = "0cd09e896e074a88dac6afb2cf2c6e1a"
                base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
                speak(" City name ")
                print("City name : ")
                city_name = takeCommand(self)
                complete_url = "http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+api_key
                response = requests.get(complete_url)
                x = response.json()

                if response.status_code == 200:
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    print(" Temperature (in kelvin unit) = " + str(
                        current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                        current_pressure) + "\n humidity (in percentage) = " + str(
                        current_humidiy) + "\n description = " + str(weather_description))

                else:
                    speak(" City Not Found ")

            elif "wikipedia" in self.query:
                webbrowser.open("wikipedia.com")

            elif "Good Morning" in self.query:
                speak("A warm" + self.query)
                speak("How are you Mister")
                speak(assname)


            elif "will you be my gf" in self.query or "will you be my bf" in self.query:
                speak("I'm not sure about, may be you should give me some time")

            elif "how are you" in self.query:
                speak("I'm fine, glad you me that")

            elif "i love you" in self.query:
                speak("It's hard to understand")

            elif "what is" in self.query or "who is" in self.query:


                client = wolframalpha.Client("K27AE5-P642A7TYKA")
                res = client.self.query(self.query)

                try:
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except StopIteration:
                    print("No results")

startExecution = MainThread()



class Main(QMainWindow):
        def __init__(self):
            super().__init__()
            self.ui = Ui_jjgui()
            self.ui.setupUi(self)
            self.ui.pushButton.clicked.connect(self.startTask)
            self.ui.pushButton_2.clicked.connect(self.close)

        def __del__(self):
            sys.stdout = sys.__stdout__

        def startTask(self):
            self.ui.movie = QtGui.QMovie("../../Downloads/7LP8.gif")
            self.ui.label.setMovie(self.ui.movie)
            self.ui.movie.start()
            self.ui.movie = QtGui.QMovie("../depositphotos_346456510-stock-illustration-letter-type-logo-design-vector.jpg")
            self.ui.label_2.setMovie(self.ui.movie)
            self.ui.movie.start()
            self.ui.movie = QtGui.QMovie("../T8bahf.gif")
            self.ui.label_3.setMovie(self.ui.movie)
            self.ui.movie.start()
            self.ui.movie = QtGui.QMovie("../lara.gif")
            self.ui.label_4.setMovie(self.ui.movie)
            self.ui.movie.start()
            timer = QTimer(self)
            timer.timeout.connect (self.showTime)
            timer.start(1000)
            startExecution.start()

        def showTime(self):
            current_time = QTime.currentTime()
            current_date = QDate.currentDate()
            label_time = current_time.toString('hh:mm:ss')
            label_date = current_date.toString(Qt.ISODate)
            self.ui.textBrowser.setText(label_date)
            self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
