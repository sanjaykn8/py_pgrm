import pyquotegen
import tkinter as tk
import random

quote_type=["funny","motivational","nature","coding"]

def gen_quote():
    val=random.choice(quote_type)
    quote=pyquotegen.get_quote(val)
    label.config(text=quote)

root = tk.Tk()
root.title("Quote Generator")
root.configure(bg="Grey")
root.geometry("600x400")

label = tk.Label(root, text="Button not clicked!", font=("Jokerman",18),height=3, wraplength=1000, justify="center",bg="Light Grey")
label.pack(pady=150) 

button = tk.Button(root, text="Click to generate!", command=gen_quote, font=("Times New Roman", 16), bg="Dark Grey")
button.pack(pady=100)

root.mainloop()