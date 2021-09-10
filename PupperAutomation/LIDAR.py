from rplidar import RPLidar

def lidarstart():
    global lidar
    port = '/dev/ttyUSB_RPLIDAR'
    lidar = RPLidar(port)
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
    iterator = lidar.iter_measures()
    i = 0
    for new_scan, quality, angle, distance in iterator:
        if angle >= 90 and angle <= 180:
            if distance != 0:
                print("Distance:", str(distance), "Angle:", str(angle)) 
                i += 1
        if i >= 1000:
            break

def lidarscan():
    iterator = lidar.iter_measures()
    i = 0
    try:
        for new_scan, quality, angle, distance in iterator:
            if angle >= 315 or angle <= 45:
                if distance != 0:
                    print("Distance:", str(distance), "Angle:", str(angle)) 
                    i += 1
    except KeyboardInterrupt:
        print("Stopping LIDAR")
        lidarstop()

def lidarstop():
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
