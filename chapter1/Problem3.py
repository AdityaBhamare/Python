import pyttsx3

# Explicitly set the driver to 'nsss' for macOS
engine = pyttsx3.init('nsss') 
engine.say("Spiderman Spiderman tune churaya mere dil ka chain ")
engine.runAndWait()