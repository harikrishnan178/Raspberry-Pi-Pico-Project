import machine
import utime

# Define HC-05 serial connection
uart = machine.UART(0, baudrate= 115200, tx=0, rx=1)
print("UART initialized")

def send_data(data):
    uart.write(data)

def receive_data():
    return uart.readline()

while True:
    # Send data to HC-05
    send_data("Hello from Pico!\n")

    # Receive data from HC-05
    received_data = receive_data()

    if received_data:
        print("Received: {}".format(received_data.decode("utf-8")))

    utime.sleep(1)
