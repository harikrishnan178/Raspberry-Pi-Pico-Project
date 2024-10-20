import machine
import utime

led0=machine.Pin(0,machine.Pin.OUT)
led1=machine.Pin(1,machine.Pin.OUT)


blink=0
while blink<=5:
    led0.on()
    utime.sleep(0.2)
    led0.off()
    utime.sleep(0.2)

    led1.on()
    utime.sleep(0.2)
    led1.off()
    utime.sleep(0.2)
    blink=blink+1
    
print("bye")



