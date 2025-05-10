import keyboard
import mouse
import time


print("off/on autoclicker alt+Q")
isClicking=False

def set_cliker():
    global isClicking
    if isClicking:
        isClicking=False
        print("clicker off")
    else:
        isClicking=True
        print("clicker on")

keyboard.add_hotkey("alt+q", set_cliker)

while True:
    if isClicking:
        mouse.double_click(button="left")
        time.sleep(0.1)