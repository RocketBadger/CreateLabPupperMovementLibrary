from rplidar import RPLidar
port = '/dev/ttyUSB_RPLIDAR'
lidar = RPLidar(port)

# info = lidar.get_info()
# print(info)

# health = lidar.get_health()
# print(health)

iterator = lidar.iter_measures()
i = 0
for new_scan, quality, angle, distance in iterator:
    # if angle >= 350 or angle <= 10:
    if distance != 0:
        print("Quality:", str(quality), "Distance:", str(distance), "Angle:", str(angle)) 
        i += 1
    if i >= 100:
        break



# for i, scan in enumerate(lidar.iter_scans()):
#     print('%d: Got %d measurements' % (i, len(scan)))
#     print(scan)
#     # for measure in scan:
#     #     if measure[1] > 0 and measure[1] < 90:
#     #         print(measure[2])
#     if i > 1:
#         break

lidar.stop()
lidar.stop_motor()
lidar.disconnect()