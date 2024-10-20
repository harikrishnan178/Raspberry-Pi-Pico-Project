from machine import Pin, PWM
import utime

# Motor A
motorA_enable = PWM(Pin(0))  # PWM pin for motor A enable
motorA_input1 = Pin(1, Pin.OUT)  # Input 1 of motor A
motorA_input2 = Pin(2, Pin.OUT)  # Input 2 of motor A

# Motor B
motorB_enable = PWM(Pin(3))  # PWM pin for motor B enable
motorB_input1 = Pin(4, Pin.OUT)  # Input 1 of motor B
motorB_input2 = Pin(5, Pin.OUT)  # Input 2 of motor B

# Function to control motor direction and speed
def control_motor(motor_enable, motor_input1, motor_input2, speed):
    motor_enable.duty_u16(speed)  # Set PWM duty cycle for speed control
    if speed > 0:
        motor_input1.on()
        motor_input2.off()
    elif speed < 0:
        motor_input1.off()
        motor_input2.on()
    else:
        motor_input1.off()
        motor_input2.off()

# Function to stop motors
def stop_motors():
    motorA_enable.duty_u16(0)
    motorB_enable.duty_u16(0)
    motorA_input1.off()
    motorA_input2.off()
    motorB_input1.off()
    motorB_input2.off()

# Main loop
while True:
    # Control Motor A
    control_motor(motorA_enable, motorA_input1, motorA_input2, 200)  # Forward at 50% speed
    utime.sleep(2)  # Run for 2 seconds
    control_motor(motorA_enable, motorA_input1, motorA_input2, -200)  # Backward at 50% speed
    utime.sleep(2)  # Run for 2 seconds

    # Control Motor B
    control_motor(motorB_enable, motorB_input1, motorB_input2, 200)  # Forward at 50% speed
    utime.sleep(2)  # Run for 2 seconds
    control_motor(motorB_enable, motorB_input1, motorB_input2, -200)  # Backward at 50% speed
    utime.sleep(2)  # Run for 2 seconds

    # Stop Motors
    stop_motors()
