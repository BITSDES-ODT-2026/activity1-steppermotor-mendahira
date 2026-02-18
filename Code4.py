from machine import Pin 

import time 

  

sm1 = Pin(14, Pin.OUT) 

sm2 = Pin(25, Pin.OUT) 

sm3 = Pin(26, Pin.OUT) 

sm4 = Pin(27, Pin.OUT) 

switch1 = Pin(4, Pin.IN, Pin.PULL_UP) 

switch2 = Pin(21, Pin.IN, Pin.PULL_UP) 

  

  

List = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]] 

  

while True: 

    if (switch1.value() == 0): 

        for i in List: 

            sm1.value(i[0]) 

            sm2.value(i[1]) 

            sm3.value(i[2]) 

            sm4.value(i[3]) 

            time.sleep(0.005) 

             

    if (switch2.value() == 0): 

        for i in reversed(List): 

            sm1.value(i[0]) 

            sm2.value(i[1]) 

            sm3.value(i[2]) 

            sm4.value(i[3]) 

            time.sleep(0.005) 

 
