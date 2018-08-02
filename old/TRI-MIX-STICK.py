#!/usr/bin/python

import Adafruit_ADS1x15, time, os

adc = Adafruit_ADS1x15.ADS1115()

FAC_S1 = (adc.read_adc(0, gain=16) + adc.read_adc(0, gain=16) + adc.read_adc(0, gain=16) + adc.read_adc(0, gain=16) + adc.read_adc(0, gain=16)) / 5 / 20.9 
FAC_S2 = (adc.read_adc(1, gain=16) + adc.read_adc(1, gain=16) + adc.read_adc(1, gain=16) + adc.read_adc(1, gain=16) + adc.read_adc(1, gain=16)) / 5 / 20.9

while True:
#   O2_S1 = round(adc.read_adc(0, gain=16) / FAC_S1,1)
#   O2_S2 = round(adc.read_adc(1, gain=16) / FAC_S2,1)
   O2_S1 = 10.6
   O2_S2 = 18.1
   O2_S1_dec = O2_S1 / 100
   O2_S2_dec = O2_S1 / 100
   HE = round((1 - O2_S2_dec) / (1 - O2_S1_dec) + O2_S1_dec * (O2_S2_dec - 1) / (0.208 * (1 - O2_S1_dec)))
   os.system('clear')
   print " "
   print " ", O2_S2,"% O2 /" "  ", HE,"% He"
   print " "
   print " ", "S1:",O2_S1,"%","  ","S2:", O2_S2, "%"
   time.sleep(0.5)
