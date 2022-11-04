
import machine

import utime


led = machine.Pin('LED', machine.Pin.OUT)
led.high()

#leftMotor = machine.Pin(16, machine.Pin.OUT) # bottom pin
class motor:
    def __init__(this, posTrans1, posTrans2, negTrans1, negTrans2):
        this.posTrans1 = machine.Pin(posTrans1, machine.Pin.OUT)
        this.posTrans2 = machine.Pin(posTrans2, machine.Pin.OUT)
        this.negTrans1 = machine.Pin(negTrans1, machine.Pin.OUT)
        this.negTrans2 = machine.Pin(negTrans2, machine.Pin.OUT)



def foward(Motor):
    Motor.posTrans2.low()
    Motor.negTrans2.low()
    Motor.posTrans1.high()
    Motor.negTrans1.high()
    
def backward(Motor):
    Motor.posTrans1.low()
    Motor.negTrans1.low()
    Motor.negTrans2.high()
    Motor.posTrans2.high()



leftMotor = motor(15, 14, 13, 12)
rightMotor = motor(16, 17, 18, 19)


leftLdr = machine.ADC(26) #bottom pin
rightLdr = machine.ADC(27) #top pin






while True:
    leftReading = leftLdr.read_u16()
    rightReading = rightLdr.read_u16()

    difference = rightReading - leftReading 

    print("ADC: ", leftReading, rightReading)
    utime.sleep(0.2)

    if(rightReading > 6000 and leftReading > 6000):
        foward(leftMotor)
        foward(rightMotor)

        print('forward')
    elif(rightReading < 6000 and leftReading < 6000):
        backward(leftMotor)
        backward(rightMotor)
        print('backwards')
    elif(rightReading < 6000):
        foward(leftMotor)
        backward(rightMotor)
        print('right')
    elif(leftReading < 6000):
        backward(leftMotor)
        foward(rightMotor)
        print('left')
    





