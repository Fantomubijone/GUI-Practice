import tkinter as tk

def button_click():
    print("Pipindot na ako")

window = tk.Tk()
window.title("Sample GUI")

b = tk.Button(window, text="Click Me", command = button_click)
b.pack()

window.mainloop()