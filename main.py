from cgitb import text
from itertools import count
from tkinter import *
from turtle import bgcolor, color, onclick
import time
import math

#CONSTANTS
PINK = "#ed979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer = None
reps = 0

#resetTimer
def resetTimer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="25:00")
    title.config(text="Timer",)


#startTimer
def startTimer():
    global reps
    reps+= 1
    if(reps%2 != 0):
        countdown(WORK_MIN*60)
        title.config(text="KEEP GRINDING", fg = "purple")
    elif(reps%8 == 0):
        title.config(text="LONG BREAK", fg = "green")
        countdown(LONG_BREAK_MIN*60)
        reps = 0
    else:
        countdown(SHORT_BREAK_MIN*60)
        title.config(text="SHORT BREAK", fg = "red")

    

#countDown
def countdown(count):
    text_min = math.floor(count/60)
    text_sec = count%60

    if text_sec<10:
        text_sec = f"0{text_sec}"
    if text_min<10:
        text_min = f"0{text_min}"

    canvas.itemconfig(timer_text, text=f"{text_min}:{text_sec}")
    
    if(count>0):
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        startTimer()



#UI Setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Canvas for Timer
canvas = Canvas(width=200, height=250,  highlightthickness=0)
backGround = PhotoImage(file="tom.png")
canvas.create_image(100, 125, image = backGround)
timer_text = canvas.create_text(100, 125, font=("Courier", 35, "bold"), text="25:00", fill="yellow")
canvas.grid(column=2,row=2)

#title
title = Label(font=("Courier", 35), text="Timer", fg = "blue", bg = YELLOW)
title.grid(column=2, row=1)

#start button
start = Button(font=("bold"), text="Start", bg="grey", highlightthickness=0, command=startTimer)
start.grid(column=1,row=3)

#reset button
reset = Button(font=("bold"), text="Reset", bg="grey", highlightthickness=0, command=resetTimer)
reset.grid(column=3, row=3)



window.mainloop()
