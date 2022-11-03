# Year 12 Electronics Assesment

robot programing files and testing documentation



if robot moves too slowly:
  1. change the gear ratios
  2. incress the battery voltage and add a voltage devider to the pico to maintain the 3.3v-5v



notes for the circuit diagram (circuitWithBackwards.png):
  1. Orange line is for the posTrans in realtion to the main.py script
  2. Green line is for the negTrans in realtion to the main.py script
  3. Ground wire on the right hand side conected to the motors is conected to ground of the battery
  4. Make sure the LDRs are conected to 3.3v power not battery power as this will change the readings and will throw off the script
