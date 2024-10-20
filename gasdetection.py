import machine
import utime


mq2=machine.ADC(26)


while True:
    smokevalue=mq2.read_u16()
    voltage=mq2.read_u16()*0.000056
    
    print("smoke value is ",smokevalue)
    print("voltage value is ",voltage)
    utime.sleep(2)