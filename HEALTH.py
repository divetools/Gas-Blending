#!/usr/bin/python

import Adafruit_ADS1x15, time, os

adc = Adafruit_ADS1x15.ADS1115()

FAC_S1 = (adc.read_adc(0, gain=16) + adc.read_adc(0, gain=16) + adc.read_adc(0, gain=16) + adc.read_adc(0, gain=16) + adc.read_adc(0, gain=16)) / 5 / 20.9 
FAC_S2 = (adc.read_adc(1, gain=16) + adc.read_adc(1, gain=16) + adc.read_adc(1, gain=16) + adc.read_adc(1, gain=16) + adc.read_adc(1, gain=16)) / 5 / 20.9

while True:
   O2_S1 = round(adc.read_adc(0, gain=16) / FAC_S1,1)
   O2_S2 = round(adc.read_adc(1, gain=16) / FAC_S2,1)
   S1 = round(adc.read_adc(0, gain=16) * 0.00781274,1)
   S2 = round(adc.read_adc(0, gain=16) * 0.00781274,1)
   os.system('clear')
   print " ", "S1:", O2_S1,'%', "     S2:", O2_S1
   print " "
   print " ", "S1:", S1,"mV"
   print " "
   print " ", "S2:", S2,"mV"
   time.sleep(0.5)