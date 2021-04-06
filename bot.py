import time
import pyautogui
import keyboard



timeout = 35
timeout_start = time.time()

time.sleep(3)

while keyboard.is_pressed('w') == False:
    while time.time() < timeout_start + timeout:
        
        im1 = pyautogui.screenshot()

        r1,g1,b1 = im1.getpixel((825, 250))
        r2,g2,b2 = im1.getpixel((925, 250))
        r3,g3,b3 = im1.getpixel((1025, 250))
        r4,g4,b4 = im1.getpixel((1125, 250))
        r5,g5,b5 = im1.getpixel((825, 350))
        r6,g6,b6 = im1.getpixel((925, 350))
        r7,g7,b7 = im1.getpixel((1025, 350))
        r8,g8,b8 = im1.getpixel((1125, 350))
        r9,g9,b9 = im1.getpixel((825, 450))
        r10,g10,b10 = im1.getpixel((925, 450))
        r11,g11,b11 = im1.getpixel((1025, 450))
        r12,g12,b12 = im1.getpixel((1125, 450))
        r13,g13,b13 = im1.getpixel((825, 550))
        r14,g14,b14 = im1.getpixel((925, 550))
        r15,g15,b15 = im1.getpixel((1025, 550))
        r16,g16,b16 = im1.getpixel((1125, 550))

        if r1 == 0:
            pyautogui.click(825, 250)
        if r2 == 0:
            pyautogui.click(925, 250)
        if r3 == 0:
            pyautogui.click(1025, 250)
        if r4 == 0:
            pyautogui.click(1125, 250)
        if r5 == 0:
            pyautogui.click(825, 350)
        if r6 == 0:
            pyautogui.click(925, 350)
        if r7 == 0:
            pyautogui.click(1025, 350)
        if r8 == 0:
            pyautogui.click(1125, 350)
        if r9 == 0:
            pyautogui.click(825, 450)
        if r10 == 0:
            pyautogui.click(925, 450)
        if r11 == 0:
            pyautogui.click(1025, 450)
        if r12 == 0:
            pyautogui.click(1125, 450)
        if r13 == 0:
            pyautogui.click(825, 550)
        if r14 == 0:
            pyautogui.click(925, 550)
        if r15 == 0:
            pyautogui.click(1025, 550)
        if r16 == 0:
            pyautogui.click(1125, 550)  
        
