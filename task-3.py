import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password(length, complexity):
    if complexity == "Low":
        characters = string.ascii_lowercase
    elif complexity == "Medium":
        characters = string.ascii_letters  # Lowercase and uppercase
    elif complexity == "High":
        characters = string.ascii_letters + string.digits  # Lowercase, uppercase, and numbers
    else:
        raise ValueError("Invalid complexity level.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def on_generate():
    try:
        length = int(length_entry.get())
        complexity = complexity_var.get()
        
        if length < 1:
            raise ValueError("The length must be at least 1.")
        
        password = generate_password(length, complexity)
        
        password_label.config(text=f"Generated Password: {password}")
    except ValueError as ve:
        messagebox.showerror("Invalid input", f"Invalid input: {ve}")

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter the desired length of the password:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

tk.Label(root, text="Select the complexity level:").pack(pady=5)
complexity_var = tk.StringVar(root)
complexity_var.set("Low")  # Default value
complexity_menu = tk.OptionMenu(root, complexity_var, "Low", "Medium", "High")
complexity_menu.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="")
password_label.pack(pady=10)

root.mainloop()
