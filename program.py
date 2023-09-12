from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

Red= LED(14)
White= LED(10)
Green= LED(6)
win=Tk()
win.title("LED BLINK")
myFont=tkinter.font.Font(family='Arial',size=12,weight="bold")

def RED_LED_ON():
	if(Red.is_lit):
		Red.off()
		redButton["text"]="TURN RED LED ON"
	else:
		Red.on()
		redButton["text"]="TURN RED LED OFF"

def WHITE_LED_ON():
	if(White.is_lit):
		White.off()
		whiteButton["text"]="TURN WHITE LED ON"
	else:
		White.on()
		whiteButton["text"]="TURN WHITE LED OFF"

def GREEN_LED_ON():
	if(Green.is_lit):
		Green.off()
		greenButton["text"]="TURN GREEN LED ON"
	else:
		Green.on()
		greenButton["text"]="TURN GREEN LED OFF"

def close():
	RPi.GPIO.cleanup()
	win.destroy()

redButton=Button(win,text="TURN RED LED ON",font=myFont,command=RED_LED_ON)
redButton.grid(row=0,column=1)

whiteButton=Button(win,text="TURN WHITE LED ON",font=myFont,command=WHITE_LED_ON)
whiteButton.grid(row=0,column=3)

greenButton=Button(win,text="TURN GREEN LED ON",font=myFont,command=GREEN_LED_ON)
greenButton.grid(row=0,column=6)

exitButton=Button(win,text="EXIT WINDOW",font=myFont,command=close,bg='red')
exitButton.grid(row=2,column=3)

win.protocol("WM_DELETE_WINDOW",close)

win.mainloop()