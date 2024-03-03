import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pyaudio


def greet():
    statement="Hello! How can I assist you today?"
    print(statement)
    engine.say(statement)
    engine.runAndWait()


def get_time():
    ct = datetime.datetime.now().strftime("%H:%M")
    statement=f'Current time is {ct}'
    print(statement)
    engine.say(statement)
    engine.runAndWait()
def get_date():
    cd = datetime.datetime.now().strftime("%Y-%m-%d")
    statement=f'Today date is{cd}'
    print(statement)
    engine.say(f'Today date is{cd}')
    engine.runAndWait()
def get_name():
    statement="my name is Omkar's assistant"
    print(statement)
    engine.say("my name is Omkar's assistant")
    engine.runAndWait()
def get_bye():
    engine.say("Bye have a nice day")
    engine.runAndWait()



def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    engine.say(f"Here is what I found for {query}")
    engine.runAndWait()


def voice_assistant():
    re = sr.Recognizer()
    mi = sr.Microphone()
    while True:
        with mi as source:
            print("Say something...")
            re.adjust_for_ambient_noise(source)
            audio = re.listen(source)
        try:
            print("Processing......")
            command = re.recognize_google(audio).lower()
            print("You said :", command)
            if "hello" in command:
                greet()
            elif "time" in command:
                get_time()
            elif "date" in command:
                get_date()
            elif "search" in command:
                query = command.split("search")[1].strip()
                search_web(query)
            elif "name" in command:
                get_name()
            elif "bye" in command:
                get_bye()
            else:
                engine.say("I'm sorry, I didn't understand that command.")
                engine.runAndWait()
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Error connecting to Google API: {e}")


if __name__ == "__main__":
    engine = pyttsx3.init()
    voice_assistant()
