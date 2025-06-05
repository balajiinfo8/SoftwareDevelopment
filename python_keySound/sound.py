import keyboard
import winsound
import os

while True:
    if keyboard.read_key() == 'a' or 'b' or 'c' or 'd' or 'e' or 'f' or 'g' or 'h' or 'i' or 'j' or 'k' or 'l' or 'm' or 'n' or 'o' or 'p' or 'q' or 's' or 't' or 'u' or 'v' or 'w' or 'x' or 'y' or 'z':
        winsound.PlaySound("mks.wav" , winsound.SND_ASYNC)
        #continue
        break
    # KP_Enter
    if keyboard.read_key() == 'KP_Enter':
        winsound.PlaySound("mks.wav" , winsound.SND_ASYNC)
        break

cmd = 'python sound.py'

os.system(cmd)
