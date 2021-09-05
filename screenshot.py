import random
import string
import time
import webbrowser

def webpage():
    rPos0 = "https://prnt.sc/"
    rPos1 = random.choice(string.ascii_letters).lower()
    rPos2 = random.choice(string.ascii_letters).lower()
    rPos3 = str((random.randint(1111,9999)))
    totalString = (rPos0 + rPos1 + rPos2 + rPos3)
    print(totalString)
    webbrowser.open(totalString)

num = int(input("How many images do you want to load? "))
for x in range(num):
    webpage()
    time.sleep(3.7)
    