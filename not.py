import machine
import utime

# Define all GPIO pins and analog pins
all_pins = [machine.Pin(pin_num, machine.Pin.OUT) for pin_num in range(29)]
analog_pin1 = machine.ADC(machine.Pin(26))
analog_pin2 = machine.ADC(machine.Pin(27))
analog_pin3 = machine.ADC(machine.Pin(28))

while True:
    # Turn on all GPIO pins
    for pin in all_pins:
        pin.value(1)
    utime.sleep(1)

    # Turn off all GPIO pins
    for pin in all_pins:
        pin.value(0)
    utime.sleep(1)

    # Read and print analog pin values
    value1 = analog_pin1.read_u16()
    value2 = analog_pin2.read_u16()
    value3 = analog_pin3.read_u16()
    print(f"Analog Pin 1 Value: {value1}")
    print(f"Analog Pin 2 Value: {value2}")
    print(f"Analog Pin 3 Value: {value3}")
