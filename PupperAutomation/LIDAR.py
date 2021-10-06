from multiprocessing import connection
from rplidar import RPLidar

class LIDAR:
    def __init__(self, injecter_connection: connection.Connection):
        self.connection = injecter_connection

        global rplidar
        # This port name has been configured by assigning fixed USB port names, to make sure the Pi finds the correct device for that USB port
        port = '/dev/ttyUSB_RPLIDAR'
        rplidar = RPLidar(port)
        print("started scanning")

    def lidarscan(self):
        iterator = rplidar.iter_measures(max_buf_meas=100000)
        while True:
            try:
                for new_scan, quality, angle, distance in iterator:
                    if angle >= 350 or angle <= 10:
                        if distance != 0:
                            # print("Distance:", str(distance), "Angle:", str(angle)) 
                            # if distance < 500:
                            self.connection.send(distance)
                            # Buffer may be clogging
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