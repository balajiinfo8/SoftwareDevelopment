import threading
from tkinter import *
import tkinter as tk
import keyboard
import winsound


def key_sound():
    while True:
        key = keyboard.read_key()
        if key in 'abcdefghijklmnopqrstucwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456790':
            winsound.PlaySound("mks.wav", winsound.SND_ASYNC)

def start_key_sound():
    thread = threading.Thread(target=key_sound,daemon=True)
    thread.start()
gui = Tk()
def close_gui():
    gui.destroy()
# change the color of background
gui.config(bg='#2596be')

button1 = Button(gui, text="play", command=start_key_sound)
button2 = Button(gui, text='close', command=close_gui)
gui.geometry("400x300")
button1.pack()
button1.place(relx=0.8, rely=0.5, anchor=tk.CENTER)
button2.pack()
button2.place(relx=0.1, rely=0.5, anchor=tk.CENTER)

# display the date
w = tk.Label(gui,text='Welcome Happy Coding')
w.pack(pady=30)
gui.mainloop()
