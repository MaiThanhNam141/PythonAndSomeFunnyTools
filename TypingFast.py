import time
import pyautogui
import keyboard

def type_text(text):
    for char in text:
        pyautogui.press(char)
        time.sleep(0.01)

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
            type_text("hello")
            keyboard.press_and_release("enter")
        else:
            if keyboard.is_pressed("enter"):
                running = True
        time.sleep(0.1)

if __name__ == "__main__":
    main()
