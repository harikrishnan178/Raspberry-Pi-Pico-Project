import machine
import utime

Define ultrasonic sensor pins
trigger_pin = machine.Pin(0, machine.Pin.OUT)
echo_pin = machine.Pin(1, machine.Pin.IN)
bazzer_pin = machine.Pin(15, machine.Pin.OUT)

def measure_distance_cm():
    # Trigger ultrasonic sensor
    trigger_pin.value(0)
    utime.sleep_us(2)
    trigger_pin.value(1)
    utime.sleep_us(10)
    trigger_pin.value(0)

    # Measure echo pulse duration
    pulse_duration = machine.time_pulse_us(echo_pin, 1, 30000)  # 30,000 µs (30 ms) timeout for 500 cm max range

    # Convert pulse duration to distance in cm
    distance_cm = (pulse_duration / 2) / 29.1  # Speed of sound in air is approximately 343 meters/second

    return distance_cm

while True:
    distance = measure_distance_cm()
    print("Distance:", distance, "cm")
    utime.sleep(1)
    if distance<50:
        bazzer_pin.on()
    else:
        bazzer_pin.off()
        