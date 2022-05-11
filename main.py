import speech_recognition as sr
from playsound import playsound
import os
r = sr.Recognizer()
ding = os.getcwd() + '/ding.mp3'
def get_audio():

    while True:
        with sr.Microphone() as source:
            print("Listening")
            try:
                audio = r.listen(source, timeout=2, phrase_time_limit= 1.5)
                said = r.recognize_google(audio, language="en-US")
                print(said)
                if(said.__contains__("Robert")):
                    print(ding)
            except sr.WaitTimeoutError as e:
                pass
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")

def lightSwitch(state):
    pass

if __name__ == "__main__":
    #get_audio()
    playsound(ding)
