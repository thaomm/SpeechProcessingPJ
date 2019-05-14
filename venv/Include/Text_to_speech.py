import pyttsx3

def tts(script):
    engine = pyttsx3.init()
    engine.say(script)
    engine.runAndWait()