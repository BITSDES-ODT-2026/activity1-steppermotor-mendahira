from machine import Pin 

import time 

  

sm1 = Pin(14, Pin.OUT) 

sm2 = Pin(25, Pin.OUT) 

sm3 = Pin(26, Pin.OUT) 

sm4 = Pin(27, Pin.OUT) 

  

  

List = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]] 

  

while True: 

    for x in range (0,1001,10): 

        x = x+1 

        for i in List: 

            sm1.value(i[0]) 

            sm2.value(i[1]) 

            sm3.value(i[2]) 

            sm4.value(i[3]) 

            time.sleep(0.005) 
