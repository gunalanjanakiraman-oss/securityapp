import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

# Female voice (Friday style)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)

engine.say("Hello. I am Friday. Voice system is now online.")
engine.runAndWait()
