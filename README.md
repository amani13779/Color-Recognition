# Color-Recognition


## Description
This project uses OpenCV to detect predefined colors in an image. The program analyzes the image, identifies specific colors, and labels each detected object.

## Tools
- Python
- OpenCV
- NumPy

## Files
- `color_recognition_plain.ipynb`
- `color.png`
- `output.png`

## How to Run

Install the required libraries:

```bash
pip install opencv-python numpy
```

Run all cells in the notebook.

## Output
The program displays the input image with each detected colored object highlighted by a green bounding box. A label showing the detected color name (Red, Blue, Green, Yellow, or Black) is placed above each object.

## Purpose
This project demonstrates how OpenCV can be used for basic color recognition using the HSV color space. It provides a simple example of image processing and object detection based on color, which can be applied in areas such as robotics, automation, and computer vision.
