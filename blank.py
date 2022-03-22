import random
import string
import os
import time
import webbrowser
from pathlib import Path
import wget
import shutil

def webpage(counter):
    rPos0 = "https://www.blank.com/photo/"
    rPos1 = urlGenerator()
    fileName = (rPos0 + rPos1)
    print(fileName)
    try:
        me = wget.download(fileName)
    except:
        print("Failed\n")

def urlGenerator():
    list1 = ["6", "7", "8"]
    list2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    list3 = ["1", "2", "3", "4", "5", "6", "7"]
    list4 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    list5 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    list6 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    list7 = ["1", "2", "3", "4", "5", "6", "7", "8"]
    list8 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    decider1 = random.choice(list1)
    decider2 = random.choice(list2)
    decider3 = random.choice(list3)
    decider4 = random.choice(list4)
    decider5 = random.choice(list5)
    decider6 = random.choice(list6)
    decider7 = random.choice(list7)
    decider8 = random.choice(list8)

    output = "8" + "1" + "6" + "1" + decider5 + decider6 + decider7 + "1" + "1"
    return output

counter = 0
x = 0
num = int(input("How many images do you want to download? "))
while x < num:
    #time.sleep(7.1)
    if (webpage(counter)) != -1:
        x += 1
        print("\nFinished downloading image " + str(x) + ", waiting 7 seconds")
        if x != num:
            time.sleep(7.1)
print("\nDownloaded " + str(x) + " photos succcessfully!")