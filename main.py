from djitellopy import Tello
from camera_controls import video
from drone_control import drone_inputs
import threading


tello = Tello()
frame_read = tello.get_frame_read()


def main():
    tello.connect()
    tello.streamon()
    smile = threading.Thread(target=video())
    control = threading.Thread(target=drone_inputs())

    smile.start()
    control.start()


if __name__ == '__main__':
    main()
