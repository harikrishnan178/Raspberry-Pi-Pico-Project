import machine
import utime


while True:
    led = machine.Pin(25,machine.Pin.OUT)
    led.on()
    utime.sleep(0.1)
    led.off()
    utime.sleep(2)