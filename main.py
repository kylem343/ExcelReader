import tkinter as tk

window = tk.Tk()

label = tk.Label(text="Python Rocks!",
                 height=6)
label.pack()

button = tk.Button(text="Press",
                   width=20,
                   height=5,
                   fg="white",
                   bg="black")
button.pack()

entry = tk.Entry(width=30)
entry.pack()

window.mainloop()


