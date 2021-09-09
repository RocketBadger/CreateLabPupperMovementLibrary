import serial
from sensors.HuskyLens.huskylib import HuskyLensLibrary
from serial.serialposix import Serial

def huskystart():
    global husky
    port = '/dev/ttyUSB_HUSKYLENS'
    husky = HuskyLensLibrary("SERIAL", port, 3000000)
    print("Woof!")
    
def huskyCount():
    husky.algorthim("ALGORITHM_FACE_RECOGNITION")
    print(husky.count())
    return husky.count()
        
# TODO
# Works but could be more elegant
def huskySniff():
    husky.algorthim("ALGORITHM_OBJECT_TRACKING")
    blocks=husky.requestAll()
    # x=0
    for block in blocks:
        print("Object ID: {} Learned: {}".format(str(block.getID()),str(block.learned)))
        if block.getID() == 1:
            husky.setCustomName("BALL", 1)
            print("BALL")
        
# saves a picture to SD Card upon finding object 
def huskyTourist():
    husky.savePictureToSDCard()
        