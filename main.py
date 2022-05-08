import speech_recognition as sr

r = sr.Recognizer()
def get_audio():

    while True:
        with sr.Microphone() as source:
            print("Listening")
            audio = r.listen(source)
            try:
                said = r.recognize_google(audio, language="en-US")
                print(said)
            except Exception as e:
                print(e)

if __name__ == "__main__":
    get_audio()