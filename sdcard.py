import machine
import utime
from chittiSat.sdcard import *
import uos

spi=machine.SPI(1,sck=machine.Pin(14),mosi=machine.Pin(15),miso=machine.Pin(12))
sd=SDCard(spi)

uos.mount(sd,'/sd')
print("sd card connected")
#with open("/sd/new.txt","w") as file:
#    file.write("hi")
print(uos.listdir('/sd'))
with open("/sd/satlite1.csv","r") as file:
    c=file.read()
    print(c)