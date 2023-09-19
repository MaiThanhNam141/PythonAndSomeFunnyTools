import time
import pyautogui
import keyboard

def stop_typing(e):
    global running
    if e.event_type == keyboard.KEY_DOWN and e.name == 'esc':
        running = False

def main():
    global running
    running = False
    keyboard.on_press(stop_typing)
    while True:
        if running:
            pyautogui.click(interval=0.0001)
        else:
            if keyboard.is_pressed("enter"):
                running = True
        time.sleep(0.0001)

if __name__ == "__main__":
    main()
