#!/usr/bin/python

# imports
import time
import RPi.GPIO as GPIO
import random
from escpos import *

# Pin Definitons:
butPin = 2 # Broadcom pin 2

# GPIO Setup
GPIO.setmode(GPIO.BCM) # Use Broadcom Layout
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

# Printer Setup
Epson = printer.Serial("/dev/ttyUSB0")

# read koizeit.db
#fobj = open("koizeit.db", "r")
#for line in fobj:
#    print line.rstrip()
#fobj.close()

data = [line.strip() for line in open("koizeit.db", 'r')]



print("Press CTRL+C to exit")
try:
     while 1:
         if ( GPIO.input(butPin) == False ):
             print("Taschd-R isch Druggdt")
             Epson.set("Center", "A", "B", 2, 2)
             Epson.text("Koi Zeit:\n\n\n")
             Epson.text(random.choice(data))
             Epson.text(" !")
             Epson.text("\n\n\n\n")
             #Epson.qr("https://www.facebook.com/schwobamemes")
             Epson.cut()
             time.sleep(2.0);

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
