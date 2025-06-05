import cmd
from tkinter import * 
import  tkinter as tk
import tkinter
import keyboard
import winsound
import os
import datetime as dtime


def key_sound():
    while True:
        if keyboard.read_key() == 'a' or 'b' or 'c' or 'd' or 'e' or 'f' or 'g' or 'h' or 'i' or 'j' or 'k' or 'l' or 'm' or 'n' or 'o' or 'p' or 'q' or 's' or 't' or 'u' or 'v' or 'w' or 'x' or 'y' or 'z':
            winsound.PlaySound("mks.wav" , winsound.SND_ASYNC)
            continue
            break
        # KP_Enter
        if keyboard.read_key() == 'KP_Enter':
            winsound.PlaySound("mks.wav" , winsound.SND_ASYNC)
            break
 
        cmd = 'python sound.py'
gui = Tk()
def close_gui():
    gui.destroy()
os.system(str(cmd))

# change the color of background
def color_change(color):
    gui.config(bg=color)
color_change("#9dede3")

button1 = Button(gui, text="play", command=key_sound)
button2 = Button(gui,text='close', command=close_gui)
gui.geometry("300x200+100+50")
button1.pack()
button1.place(relx=0.8,rely=0.5,anchor=tkinter.CENTER)
button2.pack()
button2.place(relx=0.1,rely=0.5,anchor=tkinter.CENTER)

# display the date 
date = dtime.datetime.now()
format_date = f"{date: %a,%b %b %Y}"
w = tk.Label(gui , text=format_date)
w.pack()
gui.mainloop()