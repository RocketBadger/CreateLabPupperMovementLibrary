from multiprocessing import Process, Pipe, connection
import time
from rplidar import RPLidar

class LIDAR:
    def __init__(self, injecter_connection: connection.Connection):
        self.connection = injecter_connection

    # def lidarstart():
        global rplidar
        global lidar_conn
        port = '/dev/ttyUSB_RPLIDAR'
        rplidar = RPLidar(port)
        print("Spin spin")

        print("started scanning")
        
    def lidarinfo():
        rplidar.clean_input()
        print(rplidar.get_info())
        
    def lidarhealth():
        rplidar.clean_input()
        print(rplidar.get_health())
        
    def lidarscan(self):
        # self.connection = inject_conn
        iterator = rplidar.iter_measures()
        while True:
            try:
                for new_scan, quality, angle, distance in iterator:
                    if angle >= 350 or angle <= 10:
                        if distance != 0:
                            # print("Distance:", str(distance), "Angle:", str(angle)) 
                            # if distance < 700:
                            self.connection.send(distance)
                            
                            # Buffer may be accumulating
                            # time.sleep(1)
            except KeyboardInterrupt:
                print("Stopping LIDAR")
                # self.connection.close()
                self.lidarstop()
        # self.lidarstop()


    def lidarstop(self):
        rplidar.stop()
        rplidar.stop_motor()
        rplidar.disconnect()

    def lidartest():
        for i, scan in enumerate(rplidar.iter_scans()):
            print('%d: Got %d measurements' % (i, len(scan)))
            if i > 10:
                break
        iterator = rplidar.iter_measures()
        i = 0
        for new_scan, quality, angle, distance in iterator:
            if angle >= 90 and angle <= 180:
                if distance != 0:
                    print("Distance:", str(distance), "Angle:", str(angle)) 
                    i += 1
            if i >= 1000:
                break