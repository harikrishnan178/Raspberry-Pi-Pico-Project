import machine
import utime

led0=machine.Pin(0,machine.Pin.OUT)
led1=machine.Pin(1,machine.Pin.OUT)

blink=30

while blink<50:
    led0.on()
    utime.sleep(0.2)
    led0.off()
    utime.sleep(0.2)

    led1.on()
    utime.sleep(0.2)
    led1.off()
    utime.sleep(0.2)
print("bye")



