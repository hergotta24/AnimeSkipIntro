import pyautogui
import time
# Continuously print mouse coordinates
def print_mouse_coordinates():
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Mouse coordinates: ({x}, {y})")
            time.sleep(1)  # Adjust the delay as needed
    except KeyboardInterrupt:
        print("\nStopped.")