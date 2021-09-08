import serial
from sensors.HuskyLens.huskylib import HuskyLensLibrary

def huskystart():
    global husky
    husky = HuskyLensLibrary("SERIAL", "/dev/ttyUSB1", 3000000)
    print("Woof!")
    
def huskyCount():
    print(husky.count())
    # frens = husky.count()
    # if frens > 0:
        # husky.algorthim("ALGORITHM_FACE_RECOGNITION")
        # huskyTourist()
        # huskySniff()
    return husky.count()
        
# TODO
# NOT FUNCTIONAL
def huskySniff():
    blocks=husky.requestAll()
    x=0
    # print("WOOF WOOF WOOF WOOF: " + str(blocks.getID()))
    for block in blocks:
        # print("WOOF WOOF WOOF WOOF: " + str(block.getID()))
        x=x+1
        print("Object {} data: {}".format(str(x),str(block.learned)))
    # x=0
    # for i in data:
    #     x=x+1
    #     print("Face {} data: {}".format(x,i))
        
# saves a picture to SD Card upon finding object 
def huskyTourist():
    husky.savePictureToSDCard()
        