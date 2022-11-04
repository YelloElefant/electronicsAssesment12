import machine  #importing micro python moduals to use the GPIO pins and to make the program sleep
import utime

led = machine.Pin('LED', machine.Pin.OUT)   #turns the indactor light on the Pico ON 
led.high()

class motor:    #defines a class for each motor so that each pin can be activated seperatly and to make it easy to look at
    def __init__(this, posTrans1, posTrans2, negTrans1, negTrans2):
        this.posTrans1 = machine.Pin(posTrans1, machine.Pin.OUT)
        this.posTrans2 = machine.Pin(posTrans2, machine.Pin.OUT)
        this.negTrans1 = machine.Pin(negTrans1, machine.Pin.OUT)
        this.negTrans2 = machine.Pin(negTrans2, machine.Pin.OUT)



def foward(Motor):  #defines a function that will make one of the motors turn in the forward direction
    Motor.posTrans2.low()
    Motor.negTrans2.low()
    Motor.posTrans1.high()
    Motor.negTrans1.high()
    
def backward(Motor):    #defines a function that will make one of the motors turn in the backward direction
    Motor.posTrans1.low()
    Motor.negTrans1.low()
    Motor.negTrans2.high()
    Motor.posTrans2.high()



leftMotor = motor(15, 14, 13, 12)   #defines the 2 motors based on the motor class
rightMotor = motor(16, 17, 18, 19)


leftLdr = machine.ADC(26) #bottom pin   #defines the 2 pins for the LDR light level readings
rightLdr = machine.ADC(27) #top pin






while True: #infinite loop to run the robot
    leftReading = leftLdr.read_u16()    #reading the light levels
    rightReading = rightLdr.read_u16()

    difference = rightReading - leftReading     #finding the differnce in light between each LDR

    print("ADC: ", leftReading, rightReading)   #printing the light level to the terminal
    utime.sleep(0.2)    #pausing for 0.2seconds

    if(rightReading > 6000 and leftReading > 6000): #checking if the robot should go forward 
        foward(leftMotor)   #making both motors go faward
        foward(rightMotor)
        print('forward') #printing robots movement to the terminal
    elif(rightReading < 6000 and leftReading < 6000):   #checking if the robot should go backward
        backward(leftMotor) #making both motors go backwards 
        backward(rightMotor)
        print('backwards')  #printing robots movement to the terminal
    elif(rightReading < 6000):  #checking if the robot should go right
        foward(leftMotor)   #making leftmotor go forward and rightmotor go backwards 
        backward(rightMotor)
        print('right')  #printing robots movement to the terminal
    elif(leftReading < 6000):   #checking if the robot should go left
        backward(leftMotor) #makning leftmotor go backwards and right motor go forwards
        foward(rightMotor)
        print('left')   #printing robots movement to the terminal
    





