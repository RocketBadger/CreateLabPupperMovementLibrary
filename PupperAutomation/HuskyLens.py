import serial
from sensors.huskylib import HuskyLensLibrary

def huskystart():
    global husky
    husky = HuskyLensLibrary("SERIAL", "/dev/ttyUSB0", 3000000)
    print("Woof!")
    
def huskySee():
    print(husky.knock())

def huskyCount():
    print(husky.count())