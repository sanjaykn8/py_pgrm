import tkinter as tk
from tkinter import messagebox

class InvalidInputError(Exception):
    pass

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if height <= 0 or weight <= 0:
            raise InvalidInputError("Height and Weight can't be negative!")

        bmi = weight / (height ** 2)
        category = interpret_bmi(bmi)

        result_label.config(text=f"Your BMI: {bmi:.2f}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Input Error", "Enter numeric values!")
    except InvalidInputError as e:
        messagebox.showerror("Input Error", str(e))

def interpret_bmi(bmi):
    if bmi < 15:
        return "Very Severely Underweight"
    elif 15 <= bmi < 16:
        return "Severely Underweight"
    elif 16 <= bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25<= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Moderately Obese"
    elif 35 <= bmi < 40:
        return "Severely Obese"
    else:
        return "Very Severely Obese"

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")
root.resizable(False, False)

tk.Label(root, text="Enter height (m):").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

tk.Label(root, text="Enter weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate_bmi)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Roman Text", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
