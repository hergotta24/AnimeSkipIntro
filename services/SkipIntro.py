import pyautogui
import time
import numpy as np
from PIL import ImageGrab
import pytesseract
import cv2
import re
import os

def slide_mouse_and_screenshot(start_x, start_y, end_x, end_y, duration, interval=10):
    # Set the initial position of the mouse
    try:
        time.sleep(8)
        pyautogui.moveTo(start_x, start_y)
        time.sleep(8)
        # Calculate the distance to slide
        distance = end_x - start_x

        # Slide the mouse across the X-axis
        pyautogui.dragTo(end_x, end_y, duration=duration)

        # Take screenshots every 'interval' seconds while sliding
        current_x = start_x
        while current_x < end_x:
        # Define the region above the current mouse position to take a screenshot
            screenshot_region = (current_x + 82, start_y - 30, 40, 18)
        
             # Take a screenshot of the defined region
            screenshot = pyautogui.screenshot(region=screenshot_region)
            screenshot.save(f"screenshot_{current_x}.png")  # Save the screenshot with a filename based on the current x-coordinate
        
            # Wait for 'interval' seconds
            time.sleep(interval)
        
             # Move to the next x-coordinate
            current_x += distance // (duration * 10)  # Move 1/10th of the distance each time (adjust as needed)

    except KeyboardInterrupt:
            print("\nStopped.")

first_skip = True
def default_skip_intro(x, y):
    global first_skip 
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click(x, y)
    if (first_skip == True):
        time.sleep(1)
        pyautogui.press('space')
        first_skip = False

def find_title_card(start_x, start_y, end_x, duration, title_card):
    pattern = r'= (\d+):(\d+)'
    minutes, seconds = map(int, title_card.split(':'))
    title_card_seconds = minutes * 60 + seconds 
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\hergo\AppData\Local\Programs\Tesseract-OCR\Tesseract'
    pyautogui.moveTo(start_x, start_y)

    current_x = start_x
    while current_x < end_x:
        pyautogui.moveTo(current_x + 2, start_y,.1)
        timestampImage = np.array(ImageGrab.grab(bbox=(current_x - 70, start_y - 60, current_x + 70, start_y + 20)))
        image_text = pytesseract.image_to_string(timestampImage)
        current_time = image_text_to_seconds(image_text)
        if(abs(title_card_seconds - current_time) <= 5):
            pyautogui.click(current_x, start_y)
            return
        elif(title_card_seconds - current_time > 30):
            current_x = current_x + 25
        elif(title_card_seconds - current_time > 20):
            current_x = current_x + 15
        elif(title_card_seconds - current_time > 10):
            current_x = current_x + 8
        elif(current_time > title_card_seconds):
            current_x = current_x - 5
        else:
            current_x = current_x + 2

    pyautogui.click(start_x, start_y)
    return

def image_text_to_seconds(image_text):
    string_number = re.sub(r"[^0-9]", "", image_text)
    if(len(string_number) < 3):
        return 0
    elif(len(string_number) == 3):
        minutes = int(string_number[0]) * 60
        seconds = int(string_number[1] + string_number[2])
        return minutes + seconds
    return 0
    