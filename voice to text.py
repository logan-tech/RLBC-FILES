
import speech_recognition as sr
filename = "hello.M4A"
r = sr.Recognizer()
with sr.Audiofile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    print(text)
