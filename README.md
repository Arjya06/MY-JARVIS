🤖 JARVIS – Python Voice Assistant

A customizable AI Voice Assistant built using Python that can listen to voice commands and perform system automation tasks like opening applications, playing YouTube videos, generating PDFs, launching camera, and more.

This project demonstrates Speech Recognition, Text-to-Speech, and System Automation integration.

🚀 Features

✅ Voice Command Recognition
✅ Text-to-Speech Response
✅ Open Any Installed Application
✅ Play YouTube Videos
✅ Open Google / Browser
✅ Generate PDF Files
✅ Open Camera
✅ Open Files & Folders
✅ Fully Customizable Commands

🧠 Technologies Used

Python 3.x

SpeechRecognition

pyttsx3 (Text-to-Speech)

pywhatkit (YouTube automation)

sounddevice (Microphone Input)

OpenCV (Camera access)

ReportLab (PDF generation)

OS Module (System automation)

📂 Project Structure
Jarvis/
│
├── jarvis.py
├── README.md
├── requirements.txt (optional)
└── jarvis_created.pdf (Generated during runtime)

⚙️ Installation Guide
1️⃣ Clone Repository
git clone https://github.com/yourusername/jarvis-voice-assistant.git
cd jarvis-voice-assistant

2️⃣ Create Virtual Environment (Recommended)
python -m venv .venv


Activate Environment:

Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

Windows (CMD)
.venv\Scripts\activate

3️⃣ Install Required Libraries
pip install SpeechRecognition pyttsx3 pywhatkit reportlab sounddevice scipy opencv-python

▶️ Running JARVIS
python jarvis.py


JARVIS will start listening for voice commands.

🎤 Available Voice Commands
🌐 Web Commands
Command	Action
Open YouTube	Opens YouTube
Open Google	Opens Chrome browser
💻 Application Commands
Command	Action
Open VS Code	Opens Visual Studio Code
Open Chrome	Opens Google Chrome
Open Valorant	Opens Valorant
Open Downloads	Opens Downloads folder
Open My Notes	Opens Notes file
📄 Utility Commands
Command	Action
Make PDF	Generates PDF file
Open Camera	Opens webcam
Stop Jarvis	Stops assistant
🛠 Customizing Applications

You can configure applications inside:

APP_PATHS = {
    "vs code": r"YOUR_PATH_HERE",
    "chrome": r"YOUR_PATH_HERE"
}


👉 To get application path:

Right-click app shortcut

Click Properties

Copy Target Path

📸 Camera Control

Say:

Open camera


Press Q to close camera window.

📄 PDF Generation

Say:

Make PDF


JARVIS will generate:

jarvis_created.pdf

🔧 Troubleshooting
Microphone Not Working

✔ Check Windows microphone permissions
✔ Ensure default input device is set

sounddevice Error

Run:

pip install sounddevice scipy

Speech Recognition Issues

Check internet connection (Google speech API requires it).

🌟 Future Improvements

ChatGPT / AI Conversation Integration

Smart Home Automation

GUI Interface

Android Integration via ADB

Dynamic App Detection

Wake Word Detection

Multi-Language Support

🤝 Contribution

Contributions are welcome!

Fork Repository

Create New Branch

Submit Pull Request

📜 License

This project is open-source and available under the MIT License.

If you like this project, ⭐ star the repository!

👨‍💻 Author

Arjya
