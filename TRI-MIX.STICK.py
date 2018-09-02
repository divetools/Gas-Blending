#!/usr/bin/python

from Tkinter import *
import Adafruit_ADS1x15
import time
adc = Adafruit_ADS1x15.ADS1115()

FAC_S0 = (adc.read_adc(0, gain=16) + adc.read_adc(0, gain=16) + adc.read_adc(0, gain=16) + adc.read_adc(0, gain=16) + adc.read_adc(0, gain=16)) / 5 / 20.9
FAC_S1 = (adc.read_adc(1, gain=16) + adc.read_adc(1, gain=16) + adc.read_adc(1, gain=16) + adc.read_adc(1, gain=16) + adc.read_adc(1, gain=16)) / 5 / 20.9

def get_O2_S0():
	O2_S0 = round((adc.read_adc(0, gain=16) + adc.read_adc(0, gain=16) + adc.read_adc(0, gain=16) + adc.read_adc(0, gain=16) + adc.read_adc(0, gain=16)) / 5 / FAC_S0,1)
	return (O2_S0)

def get_O2_S1():
	O2_S1 = round((adc.read_adc(1, gain=16) + adc.read_adc(1, gain=16) + adc.read_adc(1, gain=16) + adc.read_adc(1, gain=16) + adc.read_adc(1, gain=16)) / 5 / FAC_S1,1)
        return (O2_S1)

class App:

	def __init__(self, master):
		self.master = master
		frame = Frame(master)
		frame.pack()
		label = Label(frame, text='TRI-MIX Stick', font=("Helvetica", 32))
		label.grid(row=0)

		self.S0_reading_label = Label(frame, text='12.34', font=("Helvetica", 64))
		self.S0_reading_label.grid(row=1,column=0)

		self.S0_mod_label = Label(frame, text='123', font=("Helvetica", 64))
		self.S0_mod_label.grid(row=2)

                self.S1_reading_label = Label(frame, text='12.34', font=("Helvetica", 64))
                self.S1_reading_label.grid(row=1,column=1)

                self.S1_mod_label = Label(frame, text='123', font=("Helvetica", 64))
                self.S1_mod_label.grid(row=4)
		
		label = Label(frame, text="TRI-MIX STICK", font=("Helvetica", 32))
		label.grid(row=5)

		self.update_S0_reading()
		self.update_S0_mod()
                self.update_S1_reading()
                self.update_S1_mod()

	def update_S0_reading(self):
		O2_S0 = get_O2_S0()
		reading_str = "{:.2f}% O2".format(O2_S0)
		self.S0_reading_label.configure(text=reading_str)
		self.master.after(500, self.update_S0_reading)

	def update_S0_mod(self):
		MOD_S0 = round(((1.4 / (get_O2_S0() * .01)) - 1) * 33)
		mod_str = "MOD = {}".format(MOD_S0)
		self.S0_mod_label.configure(text=mod_str)
		self.master.after(500, self.update_S0_mod)

        def update_S1_reading(self):
                O2_S1 = get_O2_S1()
                reading_str = "{:.2f}% O2".format(O2_S1)
                self.S1_reading_label.configure(text=reading_str)
                self.master.after(500, self.update_S1_reading)

        def update_S1_mod(self):
                MOD_S1 = round(((1.4 / (get_O2_S1() * .01)) - 1) * 33)
                mod_str = "MOD = {}".format(MOD_S1)
                self.S1_mod_label.configure(text=mod_str)
                self.master.after(500, self.update_S1_mod)


root = Tk()
root.wm_title('ADC')
app = App(root)
root.geometry("800x450+0+0")
root.mainloop()
