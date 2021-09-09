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
    if angle > 0 and angle < 90:
        if distance > 0:
            print("Distance:", str(distance))
        i = i + 1
    if i >= 10:
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