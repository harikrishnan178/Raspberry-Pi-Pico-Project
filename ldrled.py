import machine
import utime

sensor = machine.ADC(machine.Pin(26))
led = machine.PWM(machine.Pin(15))

while True:
    utime.sleep(0.1)
    value = sensor.read_u16()

    # Map LDR value to PWM duty cycle (0-65535)
    duty_cycle = int((value / 65535) * 65535)

    # Set LED intensity
    led.freq(1000)  # Set PWM frequency to 1000 Hz
    led.duty_u16(duty_cycle)

    # Print LDR value and LED intensity for debugging
    print("LDR Value:", value, "\tLED Intensity:", duty_cycle)
