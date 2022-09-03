
import machine

import utime


led = machine.Pin('LED', machine.Pin.OUT)
led.high()

#leftMotor = machine.Pin(16, machine.Pin.OUT) # bottom pin
class motor:
    def forward(this):
        this.posTrans1.high()

    def backwards(this):
        this.posTrans1.low()

    def __init__(this, posTrans1, posTrans2, negTrans1, negTrans2):
        this.posTrans1 = machine.Pin(posTrans1, machine.Pin.OUT)
        this.posTrans2 = machine.Pin(posTrans2, machine.Pin.OUT)
        this.negTrans1 = machine.Pin(negTrans1, machine.Pin.OUT)
        this.negTrans2 = machine.Pin(negTrans2, machine.Pin.OUT)



        





rightMotor = motor(16, 17, 18, 19)
leftMotor = motor(15, 14, 13, 12)


leftLdr = machine.ADC(26) #bottom pin
rightLdr = machine.ADC(27) #top pin






while True:
    leftReading = leftLdr.read_u16()
    rightReading = rightLdr.read_u16()

    difference = rightReading - leftReading 

    print("ADC: ", leftReading, rightReading)
    utime.sleep(0.2)

    if(rightReading > 2000 and leftReading > 2000):
        leftMotor.forward()
        rightMotor.forward()
        print('forward')
    elif(rightReading < 2000):
        leftMotor.forward()
        rightMotor.backwards()
        print('right')
    elif(leftReading < 2000):
        leftMotor.backwards()
        rightMotor.forward()
        print('left')
    





