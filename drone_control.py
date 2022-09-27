from controller import XboxController
from djitellopy import Tello
import logging

Tello.LOGGER.setLevel(logging.DEBUG)

tello = Tello()
controller = XboxController()


def drone_inputs():
    tello.connect()
    print("takeoff")

    while True:
        # gets values from controller. Used to determine what drone does
        read = controller.mod_read()
        # [lj_x: 1 > float > -1, lj_y, rj_x, rj_y, rt, lt, btnA, rb, lb]

        if read['rb'] == 1:
            tello.takeoff()

        if read['lb'] == 1:
            tello.land()

        if read['btnA'] == 1:
            print("Stopping")
            tello.emergency()
            exit(1)

        # if the left joystick is moved left, take that value and turn it into "a"
        if read['lj_x'] > 0:
            d = read['lj_x']

        # if the left joystick moves right, take that value and turn it into "a"
        elif read['lj_x'] < 0:
            d = read['lj_x']

        # if left joystick hasn't moved, a is zero(this isn't necessary)
        else:
            d = 0

        #
        if read['rj_y'] > 0:
            b = read['rj_y']
        elif read['rj_y'] < 0:
            b = read['rj_y']
        else:
            b = 0

        c = read['rt'] - read['lt']

        if read['rj_x'] > 0:
            a = read['rj_x']
        elif read['rj_x'] < 0:
            a = read['rj_x']
        else:
            a = 0

        left_right_velocity = int(a * 100)
        forward_backward_velocity = int(b * 100)
        up_down_velocity = int(c * 100)
        yaw_velocity = int(d * 100)

        print(f"rc {left_right_velocity} {forward_backward_velocity} {up_down_velocity} {yaw_velocity}")

        tello.send_command_without_return(
            f"rc {left_right_velocity} {forward_backward_velocity} {up_down_velocity} {yaw_velocity}")


if __name__ == "__main__":
    # tello.connect()
    drone_inputs()
    # tello.takeoff()
    # while True:
    # video()
    # key = cv2.waitKey(1) & 0xff
    # drone_inputs()
