from rplidar import RPLidar
port = '/dev/ttyUSB_RPLIDAR'
lidar = RPLidar(port)

iterator = lidar.iter_measures()
i = 0
for new_scan, quality, angle, distance in iterator:
    if distance != 0:
        print("Quality:", str(quality), "Distance:", str(distance), "Angle:", str(angle)) 
        i += 1
    if i >= 10:
        break

lidar.stop()
lidar.stop_motor()
lidar.disconnect()