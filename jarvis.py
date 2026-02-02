import speech_recognition as sr
import pyttsx3
import pywhatkit
import os
from reportlab.pdfgen import canvas
import sounddevice as sd
import scipy.io.wavfile as wavfile
import tempfile
import cv2

# ------------ CONFIG: APP PATHS (EDIT THESE) ------------

APP_PATHS = {
    # Games / Apps – change paths to match your system
    "valorant": r"C:\Riot Games\VALORANT\live\VALORANT.exe",  # update if different
    "visual studio code": r"C:\Users\arjya\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "vs code": r"C:\Users\arjya\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "spotify": r"C:\Users\arjya\AppData\Local\Microsoft\WindowsApps\Spotify.exe",

    # Files / Folders
    "downloads": r"C:\Users\arjya\Downloads",
    "notes": r"C:\Users\arjya\Desktop\notes.pdf",  # your notes file
}

# ------------ CORE VOICE ENGINE ------------

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    duration = 5  # seconds to listen
    speak("Listening")

    # record audio using sounddevice (no PyAudio)
    fs = 16000
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    # save to temporary WAV file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wavfile.write(f.name, fs, audio_data)
        temp_name = f.name

    with sr.AudioFile(temp_name) as source:
        audio = r.record(source)

    try:
        command = r.recognize_google(audio)
        return command.lower()
    except:
        return ""

# ------------ MAIN LOOP ------------

while True:
    command = take_command()

    # Fixed commands
    if "open youtube" in command:
        speak("Opening YouTube")
        pywhatkit.playonyt("youtube")  # opens YouTube in browser [web:26][web:29]

    elif "open google" in command:
        speak("Opening Google")
        os.system("start chrome")

    elif "make pdf" in command:
        c = canvas.Canvas("jarvis_created.pdf")
        c.drawString(100, 750, "PDF created by Jarvis")
        c.save()
        speak("PDF created successfully")

    # Generic "open X" command using APP_PATHS
    elif command.startswith("open "):
        app_name = command.replace("open ", "").strip()

        # normalize some common phrases
        if app_name == "my notes":
            app_name = "notes"
        if app_name == "downloads folder":
            app_name = "downloads"

        if app_name in APP_PATHS:
            speak(f"Opening {app_name}")
            os.startfile(APP_PATHS[app_name])  # [web:125][web:129]
        else:
            speak(f"I don't know how to open {app_name} yet")

    # Open camera
    elif "open camera" in command:
        speak("Opening camera")
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            speak("Camera could not be opened")
        else:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                cv2.imshow("Camera", frame)
                # press q to close camera window
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()  # [web:131][web:136]

    # Stop JARVIS
    elif "stop jarvis" in command:
        speak("Goodbye")
        break
