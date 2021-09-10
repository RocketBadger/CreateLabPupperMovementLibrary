from multiprocessing import Process, Pipe, connection
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
    
            # if __name__ == '__main__':
        # lidar_conn, lidar_injection_conn = Pipe()
        
        # lidar = LIDAR(lidar_injection_conn)
        # self.lidar_conn = lidar_conn
        # self.lidar = lidar
        # self.lidarscan()
        print("started scanning")
        
    # def ret_conn():
    #     return lidar_conn
        
    def lidarinfo():
        print(rplidar.get_info())
        
    def lidarhealth():
        print(rplidar.get_health())
        
    def lidarscan(self):
        # self.connection = inject_conn
        iterator = rplidar.iter_measures()
        try:
            for new_scan, quality, angle, distance in iterator:
                if angle >= 315 or angle <= 45:
                    if distance != 0:
                        # print("Distance:", str(distance), "Angle:", str(angle)) 
                        # if distance < 200:
                        self.connection.send(distance)
        except KeyboardInterrupt:
            print("Stopping LIDAR")
            self.connection.close()
            self.lidarstop()

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