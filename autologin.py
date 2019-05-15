#Python 3
import pyautogui
import time
import os
import login

print('Created by a weeb procrastinating on studying.')

print("I Will log you into FFXIV Now!")

#Opens Client
os.startfile (r"D:\Games\FF14\ffxiv.lnk") #Change To whereever your FFXIV Shortcut is
time.sleep(6)

#Enters ID and Pass
pyautogui.typewrite(login.username)
pyautogui.press('tab'); pyautogui.typewrite(login.password)

#Clicks Play
pyautogui.press(['tab', 'tab', 'tab'])
pyautogui.press('enter')
time.sleep(6)
pyautogui.press('enter')




