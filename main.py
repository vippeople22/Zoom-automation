# Made By Prashanth-up
# Modified heavily by vippeople22
# https://github.com/vippeople22/zoom-quick-join
# Specialises in Laziness
# Libraries imported
import pyautogui
import schedule
import time
import os
import json
import colorama
from colorama import Fore, Style


hashes = '#' * 90
os.system('cls')
print('Welcome to the automatic zoom join thing, this project is originally from Prashanth on Github')
print('Check out his project https://github.com/prashanth-up/Zoom-Automation')
print('and mine :) https://github.com/vippeople22/zoom-quick-join')
print('But, I wanted a couple more features that he did not offer and cloned it and made my own!')
print(Fore.YELLOW + 'Please consider setting up the Class1.json file with your details to make setup easier :)')
print('Update! Now supports up to 3 classes.')
print(Fore.RED + 'Modify the main.py sleep values to better suit your systems performance')
time.sleep(0.1)

# Check if user wants to load a json file with their meet details or input manually

foo = input(Fore.MAGENTA + 'Load values from preexisting json files? (y/n): ')
print(Style.RESET_ALL)
if foo == 'y':
    bar = input('Load from class1, class2, or class3.json? (1/2/3)')
    if bar == '1':
        with open("Class1.json") as c1:
            config = json.load(c1)
        MeetingID = config["MeetingID"]
        Password = config["Password"]
        MeetTime = config["MeetTime"]
        LeaveTime = config["LeaveTime"]
    elif bar == '2':
        with open("Class2.json") as c2:
            config = json.load(c2)
        MeetingID = config["MeetingID"]
        Password = config["Password"]
        MeetTime = config["MeetTime"]
        LeaveTime = config["LeaveTime"]
    elif bar == '3':
        with open("Class3.json") as c3:
            config = json.load(c3)
        MeetingID = config["MeetingID"]
        Password = config["Password"]
        MeetTime = config["MeetTime"]
        LeaveTime = config["LeaveTime"]
elif foo == 'n':
    # get values
    print('\n\n' + hashes)
    print(Fore.YELLOW + 'This will have to be repeated every time upon startup')
    print(Style.RESET_ALL)
    print('Please modify the Class1.json file to have an easier time starting up')
    print(hashes, '\n')
    print('Input values')
    MeetingID = input('Enter Meeting ID: ')
    Password = input('Enter Meeting password: ')
    MeetTime = input('Enter everyday meeting in 24h with leading 0 before 10 AM: ')
    LeaveTime = input('Enter time to kill zoom via command prompt (ensure you have access): ')

print(hashes)

# just for confirmation
MeetTime = str(MeetTime)
print(f'Meeting ID: {MeetingID}')
print(f'Password to be entered: {Password}')

# Where the Magic happens function


def zoom():
    time.sleep(0.2)
    print('zoom init')
    pyautogui.press('esc', interval=0.1)
    print('Opening zoom')
    time.sleep(0.3)
    pyautogui.press('win', interval=0.5)
    pyautogui.write('zoom')
    time.sleep(1)
    pyautogui.press('enter', interval=0.5)
    time.sleep(3)
    print('Joining')
    x, y = pyautogui.locateCenterOnScreen('joinIMG.png', confidence=0.8)
    pyautogui.click(x, y)
    print('Entering ID')
    pyautogui.press('enter', interval=5)
    pyautogui.write(MeetingID)
    pyautogui.press('enter', interval=5)
    print('... and password')
    pyautogui.write(Password)
    pyautogui.press('enter', interval=10)
    print(f'Session has started and will continue until {LeaveTime}.')

    print('Hold (Ctrl+c) to exit the program and abort automatic leaving')


def kill():
    os.system("taskkill /f /im zoom.exe")


schedule.every().day.at("%s" % MeetTime).do(zoom)
print("Scheduling everyday at ", MeetTime)

schedule.every().day.at("%s" % LeaveTime).do(kill)
print("killing zoom at ", LeaveTime)


while True:

    # Check whether a scheduled task is pending to run or not
    schedule.run_pending()
    time.sleep(1)
