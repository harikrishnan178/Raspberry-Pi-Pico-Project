import machine
import utime

led=machine.Pin(0,machine.Pin.OUT)
buzzar=machine.Pin(1,machine.Pin.OUT)
sensor=machine.Pin(19,machine.Pin.IN,machine.Pin.PULL_DOWN)

while True:
    utime.sleep(0.1)
    if sensor.value()==1:
        led.on()
        buzzar.on()
        print("magnet detected")
    else:
        led.off()
        buzzar.off()
        print("magnet not detected")
                                                                