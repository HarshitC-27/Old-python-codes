import pyautogui
import time
time.sleep(2)
count=0
while count<=10:
    pyautogui.typewrite("hello bete");
    pyautogui.press("enter")
    count=count+10