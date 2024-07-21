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


nova_mode = ["command", "normal", "friend", "hacking"]
master_name = "kamlesh"


# inetilizening text to speech block engien
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

# this function is recognice speech and convert to text


def speech_to_text():
    recognizer = sr.Recognizer()
    # print(sr.Microphone.list_working_microphones())
    with sr.Microphone(device_index=0) as speech_source:
        recognizer.adjust_for_ambient_noise(speech_source)
        recognizer.dynamic_energy_threshold=True
        recognizer.energy_threshold =250
        # recognizer.non_speaking_duration(1000.0)
        # recognizer.operation_timeout()
        while True:
            print("I AM LISINGING......")
            try:
                audio =  recognizer.listen(speech_source)
                print("recognizing....")
                # data =recognizer.recognize_amazon(audio)
                # data= recognizer.recognize_google_cloud(audio)
                data= recognizer.recognize_google(audio)
                print("recognized....")
                print(f"user said: {data}")
                return str(data)
            except sr.UnknownValueError as e:
                # print(data)
                # print("not undarstanding")
                text_to_speech("can not understand,please repeat")
            except sr.RequestError as e:
                return str("No network hear,please connect to network ")
            except Exception as e:
                print(e.__doc__)
            # print(data)


# this function convert text to speech
def text_to_speech(textdata):

    engine.say(textdata)
    engine.runAndWait()
# ...................function to send email to person................


def sendGmail(to, content):
    print(to)
    print(content)
    my_gmail__id = "rkjrk514@gmail.com"
    my_gmail_password = 'ossfsrpjwnydzwfh'
    mail_server = smtplib.SMTP('smtp.gmail.com', 587)
    mail_server.ehlo()
    mail_server.starttls()
    mail_server.login(user=my_gmail__id, password=my_gmail_password)
    mail_server.sendmail(my_gmail__id, to, content)
    mail_server.close()


def getReciverNumber():
    country_alias = "+91"
    print("plese provide me reciver number\n")
    text_to_speech("plese provide me reciver number")
    num = speech_to_text().replace(" ", "")
    num = num.strip()
    print(num)
    while not num.isnumeric():
        text_to_speech("plese provide me reciver number")
        num = speech_to_text().replace(" ", "")
        num = num.strip()
        print(num)
    to = country_alias+num
    print(f"reciver number {to}\n")
    return to

def getPersonName():
    print("plese provide me Person name\n")
    text_to_speech("plese provide me Person name")
    name = speech_to_text().replace(" ", "")
    name = name.strip()
    print(name)
    while not name.isalpha():
        text_to_speech("plese provide me Person name")
        name = speech_to_text().replace(" ", "")
        name = name.strip()
        print(name)
    print(f"reciver name {name}\n")
    isnamecorrect = 0
    counttry=3
    while isnamecorrect == 0 and counttry > 0:
        text_to_speech(f"reciver name is {name}, is it correct?")
        isnamecorrectRes = speech_to_text()
        if "yes".lower() in isnamecorrectRes:
            isnamecorrect = 1
            break
        else:
            counttry-=1
            if counttry == 1:
                 text_to_speech("there is issue in my AI System Engine")
                 text_to_speech("so you can provide name in terminal")
                 name=input("Enter name here :")
                 break
            
            text_to_speech("please provide me correct name")
            name = speech_to_text().replace(" ", "")
            name = name.strip()
            print(name)
            while not name.isalpha():
                text_to_speech("plese provide me Person name")
                name = speech_to_text().replace(" ", "")
                name = name.strip()
            
    return name