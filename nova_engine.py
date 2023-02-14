import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time 
import math
import matplotlib
import wikipedia
import cv2
import calendar
import encodings
import ecapture
import json
import random
import requests
import pywhatkit
import smtplib


# nova_mode =["command","normal","friend","hacking"]
# master_name="kamlesh"


# inetilizening text to speech block engien
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',150)

# this function is recognice speech and convert to text
def speech_to_text():
    recognizer=sr.Recognizer()
    
    with sr.Microphone() as speech_source:
        while True:
            # recognizer.adjust_for_ambient_noise(speech_source)
            # recognizer.non_speaking_duration(1)
            # recognizer.operation_timeout()
            print("I AM LISINGING......")
            # recognizer.pause_threshold=1.5
            audio = recognizer.listen(speech_source)
            print("recognizing....")
            try:
                data = recognizer.recognize_google(audio)
                print(f"user said: {data}")
                return str(data)
            except sr.UnknownValueError as e:
                # print("not undarstanding")
                text_to_speech("can not understand,please repeat")
            except sr.RequestError as e:
                return str("No network hear,please connect to network ")
            except Exception as e:
                pass
            # print(data)
            
            
# this function convert text to speech             
def text_to_speech(textdata):
    
    engine.say(textdata)
    engine.runAndWait()
# ...................function to send email to person................

def sendGmail(to,content):
    print(to)
    print(content)
    my_gmail__id="rkjrk514@gmail.com"
    my_gmail_password='ossfsrpjwnydzwfh'
    mail_server=smtplib.SMTP('smtp.gmail.com',587)
    mail_server.ehlo()
    mail_server.starttls()
    mail_server.login(user=my_gmail__id,password=my_gmail_password)
    mail_server.sendmail(my_gmail__id,to,content)
    mail_server.close()

def getReciverNumber():
    country_alias="+91"
    text_to_speech("plese provide me reciver number")
    num=speech_to_text()
    while not num.isnumeric():
        text_to_speech("plese provide me reciver number")
        num=speech_to_text().lower()
    to=country_alias.join(num)
    print(f"reciver number {to}")
    return to
        
    