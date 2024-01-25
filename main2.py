# This speech recognition program is designed to run offline and faster using Vosk library

# import pyttsx3
import pyaudio
from vosk import Model, KaldiRecognizer
model = Model(r"C:\Users\EMMY\Downloads\vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()


# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()


while True:

    data = stream.read(4096)

    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        print(f"' {text[14:-3]} '")
