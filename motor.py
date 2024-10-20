from machine import Pin, PWM
import time

pwm_pin = 0  # PWM pin for motor speed control
cw_pin = 1  # Clockwise direction pin
acw_pin = 2  # Anti-clockwise direction pin

motor = PWM(Pin(pwm_pin))  # Create a PWM object for motor control
motor.freq(1000)  # Set PWM frequency to 1kHz

cw = Pin(cw_pin, Pin.OUT)  # Configure clockwise direction pin as output
acw = Pin(acw_pin, Pin.OUT)  # Configure anti-clockwise direction pin as output

def motor_move(speed, direction):
    if speed > 100:
        speed = 100
    elif speed < 0:
        speed = 0

    motor.duty_u16(int(speed * 65535 / 100))  # Set motor speed

    if direction < 0:
        cw.off()
        acw.on()
    elif direction > 0:
        cw.on()
        acw.off()
    else:
        cw.off()
        acw.off()

def stop_motor():
    motor.duty_u16(0)  # Stop the motor
    cw.off()
    acw.off()

def main():
    while True:
        motor_move(100, 1)  # Move motor clockwise at full speed
        time.sleep(3)  # Wait for 5 seconds
        stop_motor()
        time.sleep(3)

if __name__ == "__main__":
    main()
