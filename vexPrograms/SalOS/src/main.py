#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
left_motor_front = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
left_motor_back = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
right_motor_front = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
right_motor_back = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
intake = Motor(Ports.PORT5, GearSetting.RATIO_18_1, False)

# wait for rotation sensor to fully initialize
wait(30, MSEC)

# define variables used for controlling motors based on controller inputs
stop_left_front = False
stop_left_back = False
stop_right_front = False
stop_right_back = False

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global stop_left_front, stop_left_back, stop_right_front, stop_right_back, remote_control_code_enabled
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
            left_front_speed = controller_1.axis3.position() + controller_1.axis1.position() + controller_1.axis4.position()
            left_back_speed = controller_1.axis3.position() + controller_1.axis1.position() - controller_1.axis4.position()
            right_front_speed = controller_1.axis3.position() - controller_1.axis1.position() - controller_1.axis4.position()
            right_back_speed = controller_1.axis3.position() - controller_1.axis1.position() + controller_1.axis4.position()
            
            if left_front_speed < 5 and left_front_speed > -5:
                if stop_left_front:
                    left_motor_front.stop()
                    stop_left_front = False
            else:
                stop_left_front = True
            if left_back_speed < 5 and left_back_speed > -5:
                if stop_left_back:
                    left_motor_back.stop()
                    stop_left_back = False
            else:
                stop_left_back = True
            if right_front_speed < 5 and right_front_speed > -5:
                if stop_right_front:
                    right_motor_front.stop()
                    stop_right_front = False
            else:
                stop_right_front = True
            if right_back_speed < 5 and right_back_speed > -5:
                if stop_right_back:
                    right_motor_back.stop()
                    stop_right_back = False
            else:
                stop_right_back = True
            
            if stop_left_front:
                left_motor_front.set_velocity(left_front_speed, PERCENT)
                left_motor_front.spin(FORWARD)
            if stop_left_back:
                left_motor_back.set_velocity(left_back_speed, PERCENT)
                left_motor_back.spin(FORWARD)
            if stop_right_front:
                right_motor_front.set_velocity(right_front_speed, PERCENT)
                right_motor_front.spin(FORWARD)
            if stop_right_back:
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

# Begin project code

def toggleIntake():
  if intake.velocity(PERCENT) > 5: intake.stop()
  else: intake.spin(FORWARD)

left_motor_front.set_stopping(BRAKE)
left_motor_back.set_stopping(BRAKE)
right_motor_front.set_stopping(BRAKE)
right_motor_back.set_stopping(BRAKE)

intake.set_velocity(100, PERCENT)
controller_1.buttonA.pressed(lambda:intake.spin(FORWARD))
controller_1.buttonX.pressed(toggleIntake)
controller_1.buttonY.pressed(intake.stop)