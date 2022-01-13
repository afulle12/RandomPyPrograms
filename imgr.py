import random
import string
import os
import time
import webbrowser
from pathlib import Path
import wget
import shutil

def webpage(counter):
    rPos0 = "https://i.imgur.com/"
    rPos1 = urlGenerator()
    rPos2 = ".jpg"
    totalString = (rPos0 + rPos1 + rPos2)
    fileName = (rPos1 + rPos2)
    totalString = wget.download(totalString)
    if os.path.getsize(fileName) < 8000:
        os.remove(fileName)
        #print("\nDeleted: " + fileName + "\n")
        return -1

def urlGenerator():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num   = string.digits

    all = lower + upper + num
    list = [0, 1, 2]
    decider = random.choice(list)
    #Only selecting images in the 5 character long range is more efficient but I don't care
    if decider == 0:
        url = random.sample(all, 5)
        url = "".join(url)
        #print(url)
        return url
    if decider == 1:
        url = random.sample(all, 6)
        url = "".join(url)
        #print(url)
        return url
    if decider == 2:
        url = random.sample(all, 7)
        url = "".join(url)
        #print(url)
        return url

counter = 0;
x = 0;
num = int(input("How many images do you want to download? "))
while x < num:
    if (webpage(counter)) != -1:
        x += 1
        print("\nFinished downloading image " + str(x) + ", waiting 7 seconds")
        if x != num:
            time.sleep(7.1)
print("\nDownloaded " + str(x) + " photos succcessfully!")
