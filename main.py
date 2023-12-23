import pyautogui
import os
import time
import cv2
from services.util.PrintMouseCoords import print_mouse_coordinates
import services.SkipOutro as outro
import services.SkipIntro as intro 

if __name__ == "__main__":
    save_folder = "screenshots"  # Folder path to save screenshots
    template_image_path = "OutroTemplate/template_image.png"  #Path to the template image you want to find
    click_x, click_y = 67, 1373  # Coordinates of Crunchry Roll Next Btn on my Monitor

    # Start continuously taking screenshots until the image is recognized
    # outro.continuously_take_screenshots(template_image_path, click_x, click_y)
    # print("Move the mouse to see coordinates. Press Ctrl + C to stop.")
    print_mouse_coordinates()
    # #Define the start and end coordinates
    # 2460
    # start_x, start_y = 500, 1417
    # end_x, end_y = 600, 1417

    # #Slide the mouse and take screenshots every 2 seconds
    # slide_mouse_and_screenshot(start_x, start_y, end_x, end_y, duration=40, interval=30)
