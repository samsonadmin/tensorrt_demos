
"""display.py
"""


import cv2


def open_window(window_name, width, height, title):
    """Open the display window."""
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, width, height)
    cv2.setWindowTitle(window_name, title)


def show_help_text(img, help_text):
    """Draw help text on image."""
    cv2.putText(img, help_text, (11, 20), cv2.FONT_HERSHEY_PLAIN, 1.0,
                (32, 32, 32), 4, cv2.LINE_AA)
    cv2.putText(img, help_text, (10, 20), cv2.FONT_HERSHEY_PLAIN, 1.0,
                (240, 240, 240), 1, cv2.LINE_AA)
    return img


def show_fps(img, fps):
    """Draw fps number at top-left corner of the image."""
    font = cv2.FONT_HERSHEY_PLAIN
    line = cv2.LINE_AA
    fps_text = 'FPS: {:.2f}'.format(fps)
    cv2.putText(img, fps_text, (11, 30), font, 2.5, (216, 0, 115), 4, line)
    cv2.putText(img, fps_text, (10, 30), font, 2.5, (240, 240, 240), 1, line)
    return img

def show_face_det(img, dets):
    """samson- Draw detected face number at top-left corner of the image."""
    font = cv2.FONT_HERSHEY_PLAIN
    line = cv2.LINE_AA
    face_text = 'Face detected: {}'.format(len(dets))
    cv2.putText(img, face_text, (236, 30), font, 2.5, (0, 255, 0), 4, line)
    cv2.putText(img, face_text, (235, 30), font, 2.5, (240, 240, 240), 1, line)
    return img


def set_display(window_name, full_scrn):
    """Set disply window to either full screen or normal."""
    if full_scrn:
        cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
                              cv2.WINDOW_FULLSCREEN)
    else:
        cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
                              cv2.WINDOW_NORMAL)
