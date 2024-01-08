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
    template_image_path2 = "OutroTemplate/template.png"  #Path to the template image you want to find

    click_x, click_y = 67, 1373  # Coordinates of Crunchry Roll Next Btn on my Monitor
    x4, y = 138, 2027  # Coordinates of Crunchry Roll Next Btn on my laptop
    x1, y1 = 297, 1417
    x2, y2 = 580, 2115 # default intro place
    x3, y3 = 623, 2114
    # end_x, end_y = 600, 1417
    # start_x, start_y = 500, 1417
    #outro.continuously_grab_image("Something")
    print("Starting Application.... Switch Tabs to Begin Binging!")
    for x in range(8, 0, -1):
        print("Starting automation in " + str(x) + " seconds")
        time.sleep(1)
    while True:
        intro.default_skip_intro(x3, y3)
        intro.find_title_card(x3, y3, x3 + 400, y3, "4:20")
        # outro.continuously_take_screenshots(template_image_path2, x, y)
        outro.continuously_grab_images(template_image_path2, x4, y)
        time.sleep(4)


   
