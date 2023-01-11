#!/usr/bin/python
from escpos.printer import Usb

def print_unlock_receipt(unlock_code):
	try:
		p = Usb(0x0416, 0x5011)
		#p.text("\n")
		p.image("Yeti head.png")
		p.set("CENTER","A","normal",2,2,True,False)
		p.text("\n\n\nPrecisionPro +")
		p.set("CENTER","A","B",2,2,True,False)
		p.text("\nUnlock Code:\n\n")
		p.set("CENTER","A","B",2,2,True,True)
		p.text(" " + str(unlock_code) +" " + "\n\n\n")
		p.image("do not discard.png")
		p.text("\n\n\n\n")
		p.close()
		print("Printing complete")
	except:
		print("Failed to print")

unlock_code = input("Enter unlock code: ")

if unlock_code == "":
	unlock_code = "3xamp13c0d3"

print_unlock_receipt(unlock_code)
