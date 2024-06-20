import cv2


def set_values(x):
    """
    Default called of trackbars
    :param x: pixel value
    :return: none
    """
    print(x)


def color_trackbars():
    """
    Create taskbars need to change or adjust the marker color
    :return: none
    """
    cv2.namedWindow("Color detectors")
    cv2.createTrackbar("Upper Hue", "Color detectors", 153, 180, set_values)
    cv2.createTrackbar("Upper Saturation", "Color detectors", 255, 255, set_values)
    cv2.createTrackbar("Upper Value", "Color detectors", 255, 255, set_values)
    cv2.createTrackbar("Lower Hue", "Color detectors", 64, 180, set_values)
    cv2.createTrackbar("Lower Saturation", "Color detectors", 72, 255, set_values)
    cv2.createTrackbar("Lower Value", "Color detectors", 49, 255, set_values)