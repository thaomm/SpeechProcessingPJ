import speech_recognition as sr
import Text_to_speech

def stt():
 r = sr.Recognizer()
 m = sr.Microphone()
 with m as source:
    print("Say something!")
    Text_to_speech.tts("Say something")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

 global question
 question = r.recognize_google(audio,None,"en-US")

 print("Script: " + question)

 return question


