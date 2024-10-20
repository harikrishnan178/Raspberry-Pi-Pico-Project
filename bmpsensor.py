import machine
import utime

i2c=machine.I2C(0,scl=machine.Pin(1),sda=machine.Pin(0))
device=i2c.scan()


if device:
    print(device)