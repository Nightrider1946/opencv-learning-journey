
# Red Object Tracking with Trajectory Visualization

## Overview

This project tracks a red-colored object in real time using OpenCV.

The system detects the largest red object in the camera frame, calculates its centroid using image moments, and visualizes its movement by drawing a trajectory path.

## Features

- Real-time webcam processing
- HSV color segmentation
- Contour detection
- Largest object selection
- Centroid calculation
- Coordinate display
- Trajectory visualization

## Technologies Used

- Python
- OpenCV
- NumPy

## Working

1. Capture video from webcam.
2. Convert frame from BGR to HSV.
3. Generate mask for red color.
4. Find contours.
5. Select largest contour.
6. Calculate centroid.
7. Draw centroid and coordinates.
8. Draw trajectory showing object movement.

## Applications

- Object tracking
- Human-computer interaction
- Robotics vision systems
- Surveillance systems
