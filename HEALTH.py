#!/usr/bin/python

import Adafruit_ADS1x15, time, os

adc = Adafruit_ADS1x15.ADS1115().read_adc

FAC_S1 = (adc(0, gain=16) + adc(0, gain=16) + adc(0, gain=16) + adc(0, gain=16) + adc(0, gain=16)) / 5 / 20.9 
FAC_S2 = (adc(1, gain=16) + adc(1, gain=16) + adc(1, gain=16) + adc(1, gain=16) + adc(1, gain=16)) / 5 / 20.9

while True:
   O2_S1 = round(adc(0, gain=16) / FAC_S1,1)
   O2_S2 = round(adc(1, gain=16) / FAC_S2,1)
   S1 = round(adc(0, gain=16) * 0.00781274,1)
   S2 = round(adc(1, gain=16) * 0.00781274,1)
   S3 = round(adc(2, gain=16) * 0.00781274,1)
   S4 = round(adc(3, gain=16) * 0.00781274,1)
   os.system('clear')
   print " ", "S1:", O2_S1,'%', "     S2:", O2_S2
   print " "
   print " ", "S1:", S1,"mV"
   print " "
   print " ", "S2:", S2,"mV"
   print " "
   print " ", "S3:", S3,"mV"
   print " "
   print " ", "S4:", S4,"mV"
   time.sleep(0.5)
