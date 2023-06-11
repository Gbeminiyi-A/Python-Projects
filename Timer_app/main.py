from tkinter import *
from PIL import Image, ImageTk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
checkmark = ''
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global checkmark
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER", fg=GREEN)
    checkmark = ""
    checkmark_label.config(text=checkmark)
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global checkmark

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_min = LONG_BREAK_MIN*60

    # if it's the 8th rep
    if reps % 8 == 0:
        timer_label.config(text="BREAK", fg=RED)
        count_down(long_break_min)
        reps += 1

    # if it's the 2nd/4th/6th rep
    elif reps % 2 == 0:
        timer_label.config(text="BREAK", fg=PINK)
        checkmark = checkmark + "✔"
        checkmark_label.config(text=checkmark)
        count_down(short_break_sec)
        reps += 1

    # if it's the 1st/3rd/5th/7th rep
    else:
        timer_label.config(text="WORK", fg=GREEN)
        count_down(work_sec)
        reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer

    count_min = int(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)


    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
# window.minsize(width= 500, height=400)
window.config(pady=50, padx=100, bg=YELLOW)

# timer label, positioning and colouring and padding
timer_label = Label(text='TIMER', fg='GREEN', font=(
    FONT_NAME, 25,), bg=YELLOW, pady=20)
timer_label.grid(row=0, column=1)

# background image, positioning and colouring
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0,)
path = 'C:/Users/OLUWAGBEMINIYI/Documents/100 days of code/tomato.png'
tomato_img = PhotoImage(file=path)
canvas.create_image(103, 112, image=tomato_img,)
timer_text = canvas.create_text(
    103, 135, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'),)
canvas.grid(row=1, column=1)

# start button, positioning, padding and size
start_button = Button(text='start', relief='groove',
                      pady=5, width=10, command=start_timer)
start_button.grid(row=2, column=0)


# checkmark label, positioning, colour, and size
checkmark_label = Label(pady=30, bg=YELLOW,
                        fg=GREEN, font=(FONT_NAME, 15))
checkmark_label.grid(row=2, column=1)


# start button, positioning, padding and size
reset_button = Button(text='Reset', relief='groove', pady=5, width=10, command=reset_timer)
reset_button.grid(row=2, column=2)


# count_down(5)


window.mainloop()
