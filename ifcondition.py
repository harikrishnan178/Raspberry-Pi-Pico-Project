import machine
import utime

greenled0=machine.Pin(0,machine.Pin.OUT)
redled1=machine.Pin(1,machine.Pin.OUT)


mark=20

if mark<=35:
    print("passed")
    redled1.on()
    greenled0.off()
else:
    print("fail")
    redled1.off()
    greenled0.on()    


