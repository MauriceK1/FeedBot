import smbus
import time
from time import sleep
# for RPI version 1, use “bus = smbus.SMBus(0)”
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def readNumber():
    number = bus.read_byte(address)
    return number

while True:
    sleep(0.5)

    number = readNumber()
    print(number)