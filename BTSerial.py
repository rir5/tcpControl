import time
import sys

try:
	import serial
except:
	print "\nPlease install 'serial' google it.\n"
	SystemExit
	quit()
try:
        usbport = 'COM17'
        ser = serial.Serial(usbport, 9600, timeout=1)
except:
        print"\nCould not open: " + usbport + "\n"
        quit()

while(1):
    g = int(input("Input Serial Value: "))
    if(g == 90):
        try:
            print("Closing Port: " + usbport + "\nClosing Python Script")
            ser.close()
            sys.exit()
        except:
            quit()
    ser.write(g)
    
"""        
        
def move(angle):
    if (angle == 0):
            try:
                    print("Closing Port: " + usbport + "\nClosing Python Script")
                    ser.close()
                    sys.exit()
                    
            except:
                    quit()
                            
    if (0 <= angle <= 180):
        ser.write(chr(255))
        ser.write(chr(angle))
    else:
        print "Servo angle must be an integer between 0 and 180.\n

"""
