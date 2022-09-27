from inputs import get_gamepad
import math
import threading


class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)
    JOYSTICK_DEADZONE = .2

    def __init__(self):
        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.UpDPad = 0
        self.DownDPad = 0
        self.A = 0
        self.B = 0
        self.X = 0
        self.Y = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller,
                                                args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    def read(self):  # return the buttons/triggers that you care about in this methode
        x = self.LeftJoystickX
        y = self.LeftJoystickY
        a = self.A
        b = self.X  # b=1, x=2
        rb = self.RightBumper
        lb = self.LeftBumper
        return [x, y, a, b, rb, lb]

    def mod_read(self):
        lj_x = self.LeftJoystickX
        if abs(self.LeftJoystickX) < self.JOYSTICK_DEADZONE:
            lj_x = 0
        lj_y = self.LeftJoystickY
        if abs(self.LeftJoystickY) < self.JOYSTICK_DEADZONE:
            lj_y = 0
        rj_x = self.RightJoystickX
        if abs(self.RightJoystickX) < self.JOYSTICK_DEADZONE:
            rj_x = 0
        rj_y = self.RightJoystickY
        if abs(self.RightJoystickY) < self.JOYSTICK_DEADZONE:
            rj_y = 0
        rt = self.RightTrigger
        lt = self.LeftTrigger
        btnA = self.A
        rht_bump = self.RightBumper
        lft_bump = self.LeftBumper

        # return [lj_x, lj_y, rj_x, rj_y, rt, lt]  # List return type
        return {
            'lj_x': lj_x,
            'lj_y': lj_y,
            'rj_x': rj_x,
            'rj_y': rj_y,
            'rt': rt,
            'lt': lt,
            'btnA': btnA,
            'rb': rht_bump,
            'lb': lft_bump

        }

    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL  # normalize between -1 and 1
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL  # normalize between -1 and 1
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / XboxController.MAX_JOY_VAL  # normalize between -1 and 1
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / XboxController.MAX_JOY_VAL  # normalize between -1 and 1
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL  # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL  # normalize between 0 and 1
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_NORTH':
                    self.X = event.state
                elif event.code == 'BTN_WEST':
                    self.Y = event.state
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY1':
                    self.LeftDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY2':
                    self.RightDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY3':
                    self.UpDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY4':
                    self.DownDPad = event.state


if __name__ == '__main__':
    joy = XboxController()
    while True:
        print(joy.mod_read())
