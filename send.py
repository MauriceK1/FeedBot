import serial
import sys

ser = serial.Serial('/dev/ttyUSB0') # Change path?

for line in sys.stdin:
  out = ""
  if (line == "error"):
    out = "e"
  else:
    out = "p"
    out = out + ",".join(line.split(" "))
  ser.write(out.encode('utf-8'))