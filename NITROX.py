#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Tkinter import *
import Adafruit_ADS1x15
import time

adc = Adafruit_ADS1x15.ADS1115().read_adc

global FAC_S0
FAC_S0 = (adc(0, gain=16) + adc(0, gain=16) + adc(0, gain=16) + adc(0, gain=16) + adc(0, gain=16)) / 5 / 20.9

def get_O2_S0():
	O2_S0 = round((adc(0, gain=16) + adc(0, gain=16) + adc(0, gain=16) + adc(0, gain=16) + adc(0, gain=16)) / 5 / FAC_S0,1)
	return (O2_S0)

class App:

	def __init__(self, master):
		self.master = master
		frame = Frame(master)
		frame.pack()

                label = Label(frame, text = 'Dive Tools', font = ("Helvetica", 32))
                label.grid(row = 0)

		label = Label(frame, text='NITROX ANALYZER', font=("Helvetica", 32))
		label.grid(row=1)

		self.S0_reading_label = Label(frame, text='12.34', font=("Helvetica", 64))
		self.S0_reading_label.grid(row=2)

		self.S0_mod_label = Label(frame, text='123', font=("Helvetica", 64))
		self.S0_mod_label.grid(row=3)
		
                label = Label(frame, text="", font=("Helvetica", 32))
                label.grid(row=4)
		
		self.fac_label = Label(frame, text=FAC_S0, font=("Helvetica", 24))
		self.fac_label.grid(row=5,column=0)
		
		up_btn = Button(frame, text="+", command=self.fac_up)
		up_btn.grid(row=5, column=1)
	
                down_btn = Button(frame, text="-", command=self.fac_down)
                down_btn.grid(row=5, column=2)
		
		self.update_S0_reading()
		self.update_S0_mod()

	def update_S0_reading(self):
		O2_S0 = get_O2_S0()
		reading_str = "{:.2f}% O²".format(O2_S0)
		self.S0_reading_label.configure(text=reading_str)
		self.master.after(500, self.update_S0_reading)

	def update_S0_mod(self):
		MOD_S0 = round(((1.4 / (get_O2_S0() * .01)) - 1) * 33)
		mod_str = "MOD = {}".format(MOD_S0)
		self.S0_mod_label.configure(text=mod_str)
		self.master.after(500, self.update_S0_mod)

        def fac_up(self):
		global FAC_S0
                FAC_S0 -= .3
		self.fac_label.configure(text=FAC_S0, fg = "red")

        def fac_down(self):
		global FAC_S0
                FAC_S0 += .3
                self.fac_label.configure(text=FAC_S0, fg= "red")

root = Tk()
root.wm_title('Dive Tools --- NITROX ANALYZER')
app = App(root)
root.geometry("800x450+0+0")
root.mainloop()
