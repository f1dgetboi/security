import speech_recognition as sr
import pyttsx3
from datetime import datetime
from notify import send_mail
import picture

with open("pass.txt", "r") as file:
    password = file.read()

send_mail("s3cur1t7St3am@gmail.com",password,"fidgetman2008@gmail.com","fidgetman2008@gmail.com","test.png",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))