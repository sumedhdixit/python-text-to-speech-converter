import pyttsx3
converter = pyttsx3.init()
converter.setProperty('rate', 160)
converter.setProperty('volume', 0.7)
voices = converter.getProperty('voices')
converter.setProperty('voice', voices[1].id)
converter.say(
    "hello Everyone. I am a text to speech coverter !! "
)
converter.runAndWait()
