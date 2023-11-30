from machine import Pin,UART
import time

in1=Pin(2,Pin.OUT)
in2=Pin(3,Pin.OUT)
in3=Pin(4,Pin.OUT)
in4=Pin(5,Pin.OUT)

uart=UART(0,9600)

def right():
    in1.low()
    in2.low()
    in3.high()
    in4.low()

def left():
    in1.high()
    in2.low()
    in3.low()
    in4.low()
    
def back():
    in1.low()
    in2.high()
    in3.low()
    in4.high()    
    
def forward():
    in1.high()
    in2.low()
    in3.high()
    in4.low()
    
def stop():
    in1.low()
    in2.low()
    in3.low()
    in4.low()
def ron():
    in1.high()
    in2.low()
    in3.low()
    in4.high()
    
while True:
    if uart.any():
        data=uart.read()
        data=str(data)
        print(data)
        
        if('forward' in data):
            forward()
        elif('stop' in data):
            stop()
        elif('right' in data):
            right()
        elif('left' in data):
            left()
        elif('back' in data):
            back()
        elif('ron' in data):
            ron()
        
            
            