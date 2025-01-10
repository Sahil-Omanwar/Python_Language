#light weight jarvis to play music and open sites
import speech_recognition as sr
import webbrowser  # Built-in module, no need to install
import pyttsx3
import requests  # Correct import for making HTTP requests

# Initialize recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()
API_KEY = "28672dc8d2f34a21bc2cfea196f06b30"

# Music library dictionary
music = {
    "co2": "https://youtu.be/U2SVCCENLjE?si=KyuPSKFSoXtPHsQC",
    "tere bina": "https://youtu.be/9JDSGhhiOwI?si=u9THjsuQjbX_Z92C",
    "aaoge tum kabhi": "https://youtu.be/i96UO8-GFvw?si=1pW74nRcprUA1bKF",
    "yellow": "https://youtu.be/yKNxeF4KMsY?si=JQ382FCqbDK1xTEm",
    "iktara": "https://youtu.be/fSS_R91Nimw?si=HQy8FWsbvyM7ECXW",
    "agar tum sath ho": "https://youtu.be/sK7riqg2mr4?si=vfv3GgtGTzIY8quN",
    "kabira": "https://youtu.be/jHNNMj5bNQw?si=ovk9BIjUb1LTkVJm",
    "channa mereya": "https://youtu.be/bzSTpdcs-EI?si=cFi4-AP7zbjgj7Bt"
}

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    """Processes recognized voice command."""
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = ' '.join(c.lower().split(" ")[1:])
        if song in music:
            webbrowser.open(music[song])
        else:
            speak("Sorry, I couldn't find the song.")
    elif "news" in c.lower():
        req = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}")
        if req.status_code == 200:
            data = req.json()
            articles = data.get("articles", [])
            for article in articles:
                speak(article['title'])
        else:
            speak("Sorry, I couldn't fetch the news.")


        #let open ai handle request



if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            # Obtain audio from the microphone
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)

            # Recognize speech using Google Web Speech API
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes?")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
