from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from pathlib import Path

def textAdder(inputImage, num, myOutput):
    try:
        font = ImageFont.truetype("Pixeled.ttf", 42)
        img  = Image.open(inputImage)
        imgE = ImageDraw.Draw(img)
        imgE.text((370, 527), num, font = font, fill = (255, 255, 255), anchor="mm")# (x, y), (R, G, B), anchor "middle middle"
        img.save(myOutput)
        print("Succeeded! Image " + myOutput + " saved!")
    except:
        print("Failed!!!")

def run():

    myRange = 0
    myInput = 0

    #Runs until it gets valid input
    while myRange == 0:
        myRange = inputRangePrompt() 
    while myInput == 0:
        myInput = inputFilePrompt()

    for i in range(myRange):
        num = ('{0:04}'.format(i+1))
        myOutput = (num + myInput)
        #print(myOutput)
        textAdder(myInput, num, myOutput)

def inputRangePrompt():
    myRange = int(input("How many images do you want to generate: "))

    if myRange <= 0 or myRange > 9999:
        print("Error! You must insert a value in the range 1 to 9999!")
        return 0
    else:    
        return myRange

def inputFilePrompt():

    myInput = input("What file, in the (same directory) do you want to process? (MUST INCLUDE FILE EXTENSION) ")
    myInputP = Path(myInput)

    if myInputP.is_file():
        return myInput
    else:
        print(myInput + " is not a valid file. Please try again.")
        return 0

run()