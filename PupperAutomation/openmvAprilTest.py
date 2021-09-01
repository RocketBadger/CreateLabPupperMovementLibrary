import serial

ser = 0

def sensorOpen():
    global ser
    ser = serial.Serial('/dev/ttyACM0',9600)  # open serial port
    print(ser.name)
    
def sensorClose():
    global ser
    ser.close()
    



def sensorGetTemp():
    global ser
    
    temp=0
    print("waiting...")
    try:
        ser.flushInput()
        print("flushed input")
        temp = float(ser.readline())
        print("got temp")
    except:
        print("getTemp exception")
        pass
    return temp
   
 
    
    