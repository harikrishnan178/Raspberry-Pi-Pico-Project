import machine
import utime

# Define the pin for analog input
analog_pin = 26  # Change this to the appropriate GPIO pin

# Function to read analog value from pH sensor
def read_analog(pin):
    adc = machine.ADC(pin)
    val = adc.read_u16()  # Read the analog input (0-65535)
    return val

# Function to convert analog value to pH
def convert_to_ph(analog_val):
    # You need to calibrate this conversion according to your pH sensor's specifications
    # This is just a hypothetical conversion function
    pH = analog_val * 14.0 / 65535.0  # Assuming analog value corresponds linearly to pH (0-14)
    return pH

# Main function
def main():
    while True:
        analog_val = read_analog(analog_pin)
        pH_value = convert_to_ph(analog_val)
        #print("Raw Analog Value:", analog_val)
        print("pH Value:", pH_value)
        utime.sleep(1)  # Delay for 1 second


if __name__ == "__main__":
    main()
