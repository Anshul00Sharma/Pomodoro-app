from tkinter import *
import math
import pygame

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
NEW_RED = "#51c4d3"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 50
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 20
CHECK_MARK = '✔'
timer = None

reps = 0
start = True

# -----Alarm-----#
pygame.mixer.init()


def play():
    pygame.mixer.music.load("D:/Work/100 days python/Day28_Pomodoro/Pomodoro/beep.wav")
    pygame.mixer.music.play(2)


def stop():
    pygame.mixer.music.stop()


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    stop()
    global start, reps
    window.after_cancel(timer)
    start = True
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_mark_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    stop()
    if start:
        global reps
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if reps % 2 == 0:
            count_down(short_break_sec)
            title_label.config(text="Break", font=(FONT_NAME, 40, "bold"), fg=PINK, bg=YELLOW)
        elif reps % 8 == 0:
            count_down(long_break_sec)
            title_label.config(text="Break", font=(FONT_NAME, 40, "bold"), fg=RED, bg=YELLOW)
        else:
            count_down(work_sec)
            title_label.config(text="Work", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global start
    start = False
    min = str(int(count / 60))
    sec = count % 60
    if sec < 10:
        sec = '0' + str(sec)
    timers = f"{min}:{sec}"
    canvas.itemconfig(timer_text, text=timers)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        play()
        start = True
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += CHECK_MARK
        check_mark_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.minsize(width=480, height=500)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

tomato_img = PhotoImage(file="D:/Work/100 days python/Day28_Pomodoro/Pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))

start_button = Button(text="Start", font=(FONT_NAME, 15, "bold"), bg="#fed049", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 15, "bold"), bg="#fed049", command=reset)
reset_button.grid(column=2, row=2)

check_mark_label = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=4)
window.mainloop()
