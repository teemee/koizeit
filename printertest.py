#!/usr/bin/python
from escpos import *
Epson = printer.Serial("/dev/ttyUSB0")
# Print text
Epson.set("Center", "A", "BU", 2, 2)
Epson.text("Hello World\n\n\n\n\n\n")
# Print barcode
#Epson.barcode('1324354657687','EAN13',64,2,'','')
# Epson.qr("You can readme from your smartphone")
# Cut paper
Epson.cut()
