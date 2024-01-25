import speech_recognition as sr
import pyttsx3

# This speech recognition program runs online and cannot run offline
running = True


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def g_audio():
    r = sr.Recognizer()
    print("Listening.......")
    with sr.Microphone() as source:
        audio = r.listen(source)
        # said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
            speak(said)
        except Exception as e:
            print("Exception: " + str(e))
            speak("I am waiting")


g_audio()
