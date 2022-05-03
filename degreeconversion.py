import math
import sys
import serial

result = ""
UPPER = 19
LOWER = 13

manual = False

def getAngle(adj1, adj2, opp):
    return 180 - (math.acos( ( adj1*adj1 + adj2*adj2 - opp*opp ) / 2*adj1*adj2 ) * 180 / math.PI )

def convert(x, y, z):
    base = math.degrees(math.atan2(y, x))
    base = min(160, max(20, abs(base)))
    length = math.hypot(x, y)
    arm1 = getAngle(length, LOWER, UPPER)
    arm2 = getAngle(UPPER, LOWER, length)
    return {base, arm1, arm2}

def parse(line):
    string = ""
    words = line.split(' ')
    if (words[0] == "error"):
        string = 'e'
    elif (words[0] == "coord"):
        coord = convert(words[1], words[2], words[3])
        string = 'p' + coord[0] + ',' + coord[1] + ',' + coord[2]
    else (words[0] == "preset"):
        string = 's' + words[1]

for line in sys.stdin:
    while (arduino.in_waiting):
        data = arduino.read()
        if data == 'x':
            manual = !manual
    if (not manual):
        result = input("> ")
        arduino.write(result.encode('utf-8'))
