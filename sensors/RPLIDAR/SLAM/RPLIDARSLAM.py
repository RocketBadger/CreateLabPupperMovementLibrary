#!/usr/bin/env python3

# YOU WILL NEED X11 FORWARDING TO RUN THIS SCRIPT

MAP_SIZE_PIXELS         = 150
MAP_SIZE_METERS         = 30
LIDAR_DEVICE            = '/dev/ttyUSB_RPLIDAR'

# Ideally we could use all 250 or so samples that the RPLidar delivers in one 
# scan, but on slower computers you'll get an empty map and unchanging position
# at that rate.
MIN_SAMPLES   = 75

from breezyslam.algorithms import RMHC_SLAM
from breezyslam.sensors import RPLidarA1 as LaserModel
from rplidar import RPLidar as Lidar
from roboviz import MapVisualizer

if __name__ == '__main__':

    # Connect to Lidar unit
    lidar = Lidar(LIDAR_DEVICE)

    # Create an RMHC SLAM object with a laser model and optional robot model
    slam = RMHC_SLAM(LaserModel(), MAP_SIZE_PIXELS, MAP_SIZE_METERS)

    # Set up a SLAM display
    viz = MapVisualizer(MAP_SIZE_PIXELS, MAP_SIZE_METERS, 'SLAM')

    # Initialize an empty trajectory
    trajectory = []

    # Initialize empty map
    mapbytes = bytearray(MAP_SIZE_PIXELS * MAP_SIZE_PIXELS)

    # We will use these to store previous scan in case current scan is inadequate
    previous_distances = None
    previous_angles    = None

    i = 0
    new = True
    
    while True:
        try:
            # if True:
            if new is True:
                iterator = lidar.iter_scans(max_buf_meas=9999999999)
                # First scan is crap, so ignore it
                next(iterator)
                new = False
            
            # Extract (quality, angle, distance) triples from current scan
            items = [item for item in next(iterator)]
            print(items)
            # Extract distances and angles from triples
            distances = [item[2] for item in items]
            angles    = [item[1] for item in items]

            # Update SLAM with current Lidar scan and scan angles if adequate
            if len(distances) >= MIN_SAMPLES:
                slam.update(distances, scan_angles_degrees=angles)
                previous_distances = distances.copy()
                previous_angles    = angles.copy()

            # If not adequate, use previous
            elif previous_distances is not None:
                slam.update(previous_distances, scan_angles_degrees=previous_angles)
                
            # Get current robot position
            x, y, theta = slam.getpos()

            # Get current map bytes as grayscale
            slam.getmap(mapbytes)
            
            i = i + 1
            print (i)
            
            # Stops, resets and restarts LIDAR every fifth iteration to avoid buffer overflow
            if i % 5 is 0:
                new = True
                lidar.stop()
                lidar.reset()

            # Display map and robot pose, exiting gracefully if user closes it
            if not viz.display(x/1000., y/1000., theta, mapbytes):
                exit(0)
                
        except KeyboardInterrupt:
            # Shut down the lidar connection
            lidar.stop()
            lidar.disconnect()
