import cv2
import pyttsx3
import speech_recognition as sr
import threading
from datetime import datetime
import sys

# =======================
# FRIDAY VOICE SETUP
# =======================
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # female voice
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# =======================
# VOICE LISTEN FUNCTION
# =======================
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
    try:
        return r.recognize_google(audio).lower()
    except:
        return ""

# =======================
# FRIDAY VOICE LOOP
# =======================
def friday_voice_loop():
    speak("Friday online. Awaiting your command.")

    while True:
        command = listen()

        if "friday" in command:
            speak("Yes. How can I assist you?")

        elif "time" in command:
            speak("The time is " + datetime.now().strftime("%I:%M %p"))

        elif "date" in command:
            speak("Today is " + datetime.now().strftime("%B %d, %Y"))

        elif "exit" in command or "stop" in command:
            speak("Shutting down. Goodbye.")
            sys.exit()

# =======================
# FACE RECOGNITION (DEMO)
# =======================
def face_recognition():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        speak("Webcam not detected. Face recognition skipped.")
        return

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    speak("Face recognition started.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(
                frame,
                "Face Detected",
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        cv2.imshow("Jarvis - Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# =======================
# MAIN
# =======================
if __name__ == "__main__":
    speak("Initializing system.")

    # Start voice assistant in background
    threading.Thread(target=friday_voice_loop, daemon=True).start()

    # Start face recognition
    face_recognition()
