import os

import speech_recognition as sr
from playsound import playsound

import servo

r = sr.Recognizer()
ding = os.getcwd() + '/ding.mp3'


def get_audio():
    while True:
        with sr.Microphone() as source:
            print("Listening")
            try:
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
                said = r.recognize_google(audio, language="en-US")
                print(said)
                if (said.__contains__("Robert") or said.lower().__contains__("hopper")):
                    playsound(ding)
                    print("Now listening for light command")
                    servo.lightswitch_function()

            except sr.WaitTimeoutError as e:
                pass
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")


if __name__ == "__main__":
    get_audio()
