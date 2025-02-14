import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 115) # Lower the value slower the voice LOL
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 - male voice

try:
    with open("path to file", "r", encoding="utf-8") as file:  # Enter File Path Here
        content = file.read().strip()
    
    if content:
        engine.say(content)
        engine.runAndWait()
    else:
        print("The file is empty.")
except FileNotFoundError:
    print("Error: text.txt not found.")

engine.stop()
