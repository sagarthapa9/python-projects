# import speech_recognition as sr
# import pyttsx3

# r = sr.Recognizer()

# while True:

#     with sr.Microphone() as source:
#         print('speak now')
#         audio =  r.listen(source)
#         data = r.recognize_google(audio)
#         print(data)


# def SpeechToText(command):
#     engine = pyttsx3.init('espeak')
#     engine.say(command)
#     engine.runAndWait()


# while True:
#     try:
#         with sr.Microphone() as src:
#                 r.adjust_for_ambient_noise(src, duration=0.2)
#                 audio = r.listen(src)
#                 txt = r.recognize_google(audio).lower()
#                 print('Did you say '+ txt )
#                # SpeechToText(txt)
#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))
#     except sr.UnknownValueError:
#         print("Speak again")  

# Python program to translate 
# speech to text and text to speech 


# Python program to translate 
# text to speech 
# Install following
# pip install pyttsx3

# import pyttsx3
# import datetime

# engine = pyttsx3.init()

# t = datetime.datetime.now()
# today = datetime.date.today()
# time = t.hour,t.minute

# print('test')
# engine.say ('I\'m your personal assistant')
# engine.say ('It is currently')
# engine.say (time)
# engine.say (today)
# print('test')
# engine.runAndWait()
# print('test')

from pocketsphinx import LiveSpeech
for phrase in LiveSpeech(): print(phrase)