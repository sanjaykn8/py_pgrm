import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import tkinter as tk

engine = pyttsx3.init()
engine.setProperty('rate', 120)
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(message):
    engine.say(message)
    engine.runAndWait()

def capture_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...", fg="blue")
        root.update()
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        command_label.config(text=f"You said: {command}")
        return command
    except sr.UnknownValueError:
        command_label.config(text="Couldn't recognize speech. Try again!")
        return ""
    except sr.RequestError:
        command_label.config(text="Connection error. Check your internet.")
        return ""

def process_command(command):
    if "hello" in command:
        speak("Hey !")
        return

    if "time" in command:
        speak(f"The time is {datetime.datetime.now().strftime('%I:%M %p')}")
        return

    if "date" in command:
        speak(f"Today's date is {datetime.datetime.today().strftime('%A, %B %d, %Y')}")
        return

    if "search" in command:
        query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.bing.com/search?q={query}")
        speak(f"Search results for {query}.")
        return
    
    if "open" in command:
        query = command.replace("open", "").strip()
        webbrowser.open(f"https://www.{query}.com")
        speak(f"Opened {query}")
        return

    speak("Showing similar results.")
    webbrowser.open(f"https://www.bing.com/search?q={command}")
    speak(f"Search results for {command}.")
    return

def start_assistant():
    speak("Voice Assistant activated")
    status_label.config(text="Voice Assistant Activated!", fg="green")
    root.update()
    while True:
        user_command = capture_command()
        if "exit" in user_command:
            speak("Goodbye!")
            status_label.config(text="Voice Assistant Stopped", fg="red")
            root.update()
            break
        process_command(user_command)

def stop_assistant():
    status_label.config(text="Voice Assistant Stopped", fg="red")
    root.update()
    root.quit()

root = tk.Tk()
root.title("Voice Assistant")
root.geometry("400x300")

status_label = tk.Label(root, text="Click Start to begin", font=("Roman Text", 12))
status_label.pack(pady=10)

command_label = tk.Label(root, text="", font=("Roman Text", 12), fg="blue")
command_label.pack(pady=10)

start_button = tk.Button(root, text="Start", font=("Roman Text", 12), bg="green", fg="white", command=start_assistant)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", font=("Roman Text", 12), bg="red", fg="white", command=stop_assistant)
stop_button.pack(pady=10)

root.mainloop()
