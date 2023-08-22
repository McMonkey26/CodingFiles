#region VEXcode Generated Robot Configuration
from vex import *

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
left_motor_front = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
left_motor_back = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
right_motor_front = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)
right_motor_back = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
intake_left = Motor(Ports.PORT19, GearSetting.RATIO_18_1, True)
intake_right = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)
intake = MotorGroup(intake_left, intake_right)

# wait for rotation sensor to fully initialize
wait(30, MSEC)

# define variables used for controlling motors based on controller inputs
drivetrain_l_f_needs_to_be_stopped_controller_1 = False
drivetrain_l_b_needs_to_be_stopped_controller_1 = False
drivetrain_r_f_needs_to_be_stopped_controller_1 = False
drivetrain_r_b_needs_to_be_stopped_controller_1 = False

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global drivetrain_l_f_needs_to_be_stopped_controller_1, drivetrain_l_b_needs_to_be_stopped_controller_1, drivetrain_r_f_needs_to_be_stopped_controller_1, drivetrain_r_b_needs_to_be_stopped_controller_1, hDrive_needs_to_be_stopped_controller_1, remote_control_code_enabled
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:
            # calculate the drivetrain motor velocities from the controller joystick axies
            # move forward: lf+, lb+, rf+, rb+
            # move backwards: lf-, lb-, rf-, rb-
            # strafe left: lf-, lb+, rf+, rb-
            # strafe right: lf+, lb-, rf-, rb+
            # turn left: lf-, lb-, rf+, rb+
            # turn right: lf+, lb+, rf-, rb-
            left_front_speed = controller_1.axis3.position() + controller_1.axis4.position() + controller_1.axis1.position()
            left_back_speed = controller_1.axis3.position() - controller_1.axis4.position() + controller_1.axis1.position()
            right_front_speed = controller_1.axis3.position() - controller_1.axis4.position() - controller_1.axis1.position()
            right_back_speed = controller_1.axis3.position() + controller_1.axis4.position() - controller_1.axis1.position()
            
            # check if the value is inside of the deadband range
            if left_front_speed < 5 and left_front_speed > -5:
                # check if the left motor has already been stopped
                if drivetrain_l_f_needs_to_be_stopped_controller_1:
                    # stop the left drive motor
                    left_motor_front.stop()
                    # tell the code that the left motor has been stopped
                    drivetrain_l_f_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the left motor next
                # time the input is in the deadband range
                drivetrain_l_f_needs_to_be_stopped_controller_1 = True
            # check if the value is inside of the deadband range
            if left_back_speed < 5 and left_back_speed > -5:
                # check if the left motor has already been stopped
                if drivetrain_l_b_needs_to_be_stopped_controller_1:
                    # stop the left drive motor
                    left_motor_back.stop()
                    # tell the code that the left motor has been stopped
                    drivetrain_l_b_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the left motor next
                # time the input is in the deadband range
                drivetrain_l_b_needs_to_be_stopped_controller_1 = True
            # check if the value is inside of the deadband range
            if right_front_speed < 5 and right_front_speed > -5:
                # check if the right motor has already been stopped
                if drivetrain_r_f_needs_to_be_stopped_controller_1:
                    # stop the right drive motor
                    right_motor_front.stop()
                    # tell the code that the right motor has been stopped
                    drivetrain_r_f_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the right motor next
                # time the input is in the deadband range
                drivetrain_r_f_needs_to_be_stopped_controller_1 = True
            # check if the value is inside of the deadband range
            if right_back_speed < 5 and right_back_speed > -5:
                # check if the right motor has already been stopped
                if drivetrain_r_b_needs_to_be_stopped_controller_1:
                    # stop the right drive motor
                    right_motor_back.stop()
                    # tell the code that the right motor has been stopped
                    drivetrain_r_b_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the right motor next
                # time the input is in the deadband range
                drivetrain_r_b_needs_to_be_stopped_controller_1 = True
            
            # only tell the left front motor to spin if the values are not in the deadband range
            if drivetrain_l_f_needs_to_be_stopped_controller_1:
                left_motor_front.set_velocity(left_front_speed, PERCENT)
                left_motor_front.spin(FORWARD)
            # only tell the left back motor to spin if the values are not in the deadband range
            if drivetrain_l_b_needs_to_be_stopped_controller_1:
                left_motor_back.set_velocity(left_back_speed, PERCENT)
                left_motor_back.spin(FORWARD)
            # only tell the right front motor to spin if the values are not in the deadband range
            if drivetrain_r_f_needs_to_be_stopped_controller_1:
                right_motor_front.set_velocity(right_front_speed, PERCENT)
                right_motor_front.spin(FORWARD)
            # only tell the right back motor to spin if the values are not in the deadband range
            if drivetrain_r_b_needs_to_be_stopped_controller_1:
                right_motor_back.set_velocity(right_back_speed, PERCENT)
                right_motor_back.spin(FORWARD)
        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True
rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)



#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *
class Direc:
    def __init__(self, key: int):
        self.key = key
class Globals:
    FRONT = Direc(0)
    BACK = Direc(1)
    LEFT = Direc(2)
    RIGHT = Direc(3)
    SPEED = 20
    MODE = True

    def speedUp(): Globals.SPEED += 10
    def speedDown(): Globals.SPEED -= 10
    def toggleMode(): Globals.MODE = not Globals.MODE

def move(dist: int, direc: Direc):
    dist *= 25
    if direc == Globals.FRONT: drive([dist, dist, dist, dist], Globals.SPEED)
    elif direc == Globals.BACK: drive([-dist, -dist, -dist, -dist], Globals.SPEED)
    elif direc == Globals.LEFT: drive([-dist, dist, dist, -dist], Globals.SPEED)
    elif direc == Globals.RIGHT: drive([dist, -dist, -dist, dist], Globals.SPEED)

def turn(dist: int, direc: Direc):
    dist = int(dist*4.25)
    if direc == Globals.LEFT: drive([-dist, -dist, dist, dist], Globals.SPEED)
    elif direc == Globals.RIGHT: drive([dist, dist, -dist, -dist], Globals.SPEED)

def drive(dist: list[int], speed: int):
    left_motor_front.spin_for(FORWARD, dist[0], DEGREES, speed, PERCENT, False)
    left_motor_back.spin_for(FORWARD, dist[1], DEGREES, speed, PERCENT, False)
    right_motor_front.spin_for(FORWARD, dist[2], DEGREES, speed, PERCENT, False)
    right_motor_back.spin_for(FORWARD, dist[3], DEGREES, speed, PERCENT, False)

def intakeUp():
    while controller_1.buttonL1.pressing():
        intake.spin(FORWARD)
    intake.stop()
def intakeDown():
    while controller_1.buttonR1.pressing():
        intake.spin(REVERSE)
    intake.stop()

def buttonUp():
    if Globals.MODE: move(18, Globals.FRONT)
    else: Globals.speedUp()
def buttonDown():
    if Globals.MODE: move(18, Globals.BACK)
    else: Globals.speedDown()
def buttonLeft():
    if Globals.MODE: move(18, Globals.LEFT)
    else: turn(90, Globals.LEFT)
def buttonRight():
    if Globals.MODE: move(18, Globals.RIGHT)
    else: turn(90, Globals.RIGHT)
def buttonA(): Globals.toggleMode()
def buttonB(): pass
def buttonX(): pass
def buttonY(): pass
def buttonL1(): intakeUp()
def buttonR1(): intakeDown()
def buttonL2(): pass
def buttonR2(): pass

controller_1.buttonUp.pressed(buttonUp)
controller_1.buttonDown.pressed(buttonDown)
controller_1.buttonLeft.pressed(buttonLeft)
controller_1.buttonRight.pressed(buttonRight)
controller_1.buttonL1.pressed(buttonL1)
controller_1.buttonR1.pressed(buttonR1)
controller_1.buttonL2.pressed(buttonL2)
controller_1.buttonR2.pressed(buttonR2)
controller_1.buttonA.pressed(buttonA)
controller_1.buttonB.pressed(buttonB)
controller_1.buttonX.pressed(buttonX)
controller_1.buttonY.pressed(buttonY)

left_motor_front.set_stopping(BRAKE)
left_motor_back.set_stopping(BRAKE)
right_motor_front.set_stopping(BRAKE)
right_motor_back.set_stopping(BRAKE)
intake.set_stopping(HOLD)