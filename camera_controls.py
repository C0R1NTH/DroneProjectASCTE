from djitellopy import Tello
import cv2
import math

tello = Tello()
tello.connect()

tello.streamon()


def video():
    frame_read = tello.get_frame_read()
    img = frame_read.frame

    font = cv2.FONT_HERSHEY_SIMPLEX
    height = str(tello.get_height())
    speed = str(tello.get_speed_x())
    roll = tello.get_roll()
    pitch = tello.get_pitch()

    w = 1200
    h = 720

    cy = h / 2
    cx = w / 2

    pitch = (h / 2) - ((pitch / 180) * h)
    # Sets default pitch value to half the screen height
    roll = math.radians(roll)
    x1 = 0.0
    x2 = w

    if roll == 90 or roll == 270:
        change_y = h
    else:
        change_y = w * math.tan(roll)

    y1 = pitch + change_y / 2
    y2 = pitch - change_y / 2

    img = cv2.line(img, (int(x1), int(y2)), (int(x2), int(y1)), (0, 255, 0), 10)
    img = cv2.putText(img, height, (920, 30), font, 1, (0, 255, 0), 6, cv2.LINE_AA)
    img = cv2.putText(img, speed, (30, 30), font, 1, (0, 255, 0), 6, cv2.LINE_AA)

    cv2.imshow("drone", img)


while True:
    video()
    key = cv2.waitKey(1) & 0xff
