import whisper
import pyttsx3

model = whisper.load_model("base")
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()