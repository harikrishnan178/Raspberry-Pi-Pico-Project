import machine
import utime

led = machine.Pin(25,machine.Pin.OUT)
led.off()