# unlock-code-printer
Dev code for interfacing with POS receipt printer

## Hardware:
* Raspberry Pi 3b+
* POS-5890K 58mm thermal printer

## Dependencies:
(python 3)
* sudo apt-get update
* sudo apt-get install python3 python3-setuptools python3-pip libjpeg8-dev
* sudo pip3 install --upgrade pip
* sudo pip3 install python-escpos

## Usage:
Call `print_unlock_receipt(unlock_code)`
