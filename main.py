import speech_recognition as sr
from playsound import playsound
import servo
import os
r = sr.Recognizer()
ding = os.getcwd() + '/ding.mp3'

def get_audio():

    while True:
        with sr.Microphone() as source:
            print("Listening")
            try:
                audio = r.listen(source, timeout=2, phrase_time_limit= 2)
                said = r.recognize_google(audio, language="en-US")
                print(said)
                if(said.__contains__("Robert") or said.lower().__contains__("hopper")):
                    playsound(ding)
                    print("Now listening for light command")
                    try:
                        lights_audio = r.listen(source, timeout=10, phrase_time_limit=6)
                        lights_said = r.recognize_google(lights_audio, language="en-US")
                        if (lights_said.__contains__('on')):
                            servo.light_switch_operation(servo.LIGHT_SWITCH_STATES.ON)

                        elif (lights_said.__contains__('off')):
                            servo.light_switch_operation(servo.LIGHT_SWITCH_STATES.OFF)
                    except sr.WaitTimeoutError as e:
                        pass
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")

            except sr.WaitTimeoutError as e:
                pass
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")



if __name__ == "__main__":
    get_audio()