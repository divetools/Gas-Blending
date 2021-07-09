#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Adafruit_ADS1x15

O2_COUNT = 6
FAC_COUNT = 6
adc = Adafruit_ADS1x15.ADS1115().read_adc
global FAC_S0

def sensor_env():
        FAC_S0_CAL_INT = FAC_COUNT
        global FAC_S0
        FAC_S0 = 0
        while FAC_S0_CAL_INT > 0:
               FAC_S0 = (FAC_S0 + adc(0, gain=16))
               FAC_S0_CAL_INT = (FAC_S0_CAL_INT - 1)

        FAC_S0 = (FAC_S0 / FAC_COUNT / 20.9) 

        FAC_S1_CAL_INT = FAC_COUNT
        global FAC_S1
        FAC_S1 = 0
        while FAC_S1_CAL_INT > 0:
                FAC_S1 = (FAC_S1 + adc(1, gain=16))
                FAC_S1_CAL_INT = (FAC_S1_CAL_INT -1)

        FAC_S1 = (FAC_S1 / FAC_COUNT / 20.9)

sensor_env()


def get_O2_S0():
        O2_S0_INT = O2_COUNT
        O2_S0 = 0
        while O2_S0_INT > 0:
             O2_S0 = (O2_S0 + adc(0, gain=16))
             O2_S0_INT = (O2_S0_INT -1)

        O2_S0 = (O2_S0 / O2_COUNT / FAC_S0)
        return (O2_S0)

def get_O2_S1():
        O2_S1_INT = O2_COUNT
        O2_S1 = 0
        while O2_S1_INT > 0:
             O2_S1 = (O2_S1 + adc(1, gain=16))
             O2_S1_INT = (O2_S1_INT -1)

        O2_S1 = (O2_S1 / O2_COUNT / FAC_S1)
        return (O2_S1)
