from rplidar import RPLidar

def lidargo():
    global lidar
    lidar = RPLidar("/dev/ttyUSB0")
    print("Spin spin")
    
def lidarinfo():
    print(lidar.get_info())
    
def lidarhealth():
    print(lidar.get_health())
    
def lidartest():
    for i, scan in enumerate(lidar.iter_scans()):
        print('%d: Got %d measurements' % (i, len(scan)))
        if i > 10:
            break

def lidarstop():
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
