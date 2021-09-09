import serial
from sensors.HuskyLens.huskylib import HuskyLensLibrary
from serial.serialposix import Serial

def huskystart():
    global husky
    port = '/dev/ttyUSB_HUSKYLENS'
    husky = HuskyLensLibrary("SERIAL", port, 3000000)
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
def huskySniff():
    husky.algorthim("ALGORITHM_OBJECT_TRACKING")
    blocks=husky.requestAll()
    x=0
    for block in blocks:
        # print("WOOF WOOF WOOF WOOF: " + str(block.getID()))
        x=x+1
        print("Object ID: {} Learned: {}".format(str(block.getID()),str(block.learned)))
        if block.getID() == 1:
            husky.setCustomName("BALL", 1)
            print("BALL")
        
    # x=0
    # for i in data:
    #     x=x+1
    #     print("Face {} data: {}".format(x,i))
        
# saves a picture to SD Card upon finding object 
def huskyTourist():
    husky.savePictureToSDCard()
        