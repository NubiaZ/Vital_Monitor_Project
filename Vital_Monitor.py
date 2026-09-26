from tkinter import *
from tkinter import ttk
from PIL import Image
Image.CUBIC = Image.BICUBIC
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

global heart_rate
heart_rate = 80

root = ttkb.Window()
frame = ttk.Frame(root, padding = 10)
frame.grid()

meter = ttkb.Meter(
frame, 
metersize = 500, # Size of the meter
padding = 20, # distance between window edges
meterthickness = 50, # thickness of the meter dial
stripethickness = 0, # thickness of discrete stripes,0=Continous
bootstyle = "success", # allows you to apply pre-defined styles like primary,danger,success etc
metertype = "semi", # Semicircle ,"full" =circular

amounttotal = 140, #max value of scale =140
amountused = heart_rate, #current value


subtext = "Heart Rate",
subtextstyle = "primary", # allows you to apply pre-defined styles like primary,danger,success etc
subtextfont = "-size 20 -weight bold",


#interactive = True, #you can change meter position by mouse
)
meter.grid(column = 0, row = 0, columnspan = 2)


#buttons to increase heart rate artificially
def increase_heart_rate():
    global heart_rate
    heart_rate += 10

    if(heart_rate < 60):
        meter_color = "danger"
    elif(heart_rate > 100):
        meter_color = "warning"
    else:
        meter_color = "success"

    meter.configure(amountused=heart_rate, bootstyle=meter_color)
    
#buttons to decrease heart rate artificially
def decrease_heart_rate():
    global heart_rate
    heart_rate -= 10

    if(heart_rate < 60):
        meter_color = "danger"
    elif(heart_rate > 100):
        meter_color = "warning"
    else:
        meter_color = "success"
    
    meter.configure(amountused=heart_rate, bootstyle=meter_color)

ttk.Button(frame, text = "increase heartrate", command = increase_heart_rate).grid(column = 1, row = 1)
ttk.Button(frame, text = "decrease heartrate", command = decrease_heart_rate).grid(column = 0, row = 1)

#frame = ttk.Frame(root, padding = 70)
#frame.grid()
#ttk.Label(frame, text = "Hello World!").grid(column = 0, row = 0)
#ttk.Button(frame, text = "Quit", command = root.destroy).grid(column = 0, row = 1)
root.mainloop()