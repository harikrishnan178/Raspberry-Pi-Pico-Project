from machine import Pin
from chittiSat.mq2 import MQ2
#from chittiSat.assitant import dashboard
import utime


led=Pin(25, Pin.OUT)
sensor=MQ2(pinData = 26)
sensor.calibrate()

while True:
    GAS=sensor.readLPG()
    Smoke=sensor.readSmoke()
    Methane=sensor.readMethane()
    Hydrogen=sensor.readHydrogen()
    print("LPG: ", GAS,"  Smoke: ",Smoke,"  Methane: ",Methane,"Hydrogen",Hydrogen)
    #dashboard.sendAir(Smoke,GAS,Methane,Hydrogen)