from sensors.HuskyLens.huskylib import HuskyLensLibrary
from multiprocessing import connection

class HUSKYLENS:
    def __init__(self, injecter_connection: connection.Connection):
        self.connection = injecter_connection
        global husky
        port = '/dev/ttyUSB_HUSKYLENS'
        husky = HuskyLensLibrary("SERIAL", port, 3000000)
        print("Woof!")
        
    def huskyCount():
        husky.algorthim("ALGORITHM_FACE_RECOGNITION")
        print(husky.count())
        return husky.count()
            
    # Works but not all that well
    def huskySniff(self):
        husky.algorthim("ALGORITHM_OBJECT_TRACKING")
        while True:
            try:
                # blocks=husky.requestAll()
                for block in husky.requestAll():
                    if block.getID() == 1 and block.learned:
                        husky.setCustomName("BALL", 1)
                        self.connection.send("BALL")
            except KeyboardInterrupt:
                print("Stopping HUSKY")
                self.connection.close()

                
    # saves a picture to SD Card upon finding object 
    def huskyTourist():
        husky.savePictureToSDCard()
            