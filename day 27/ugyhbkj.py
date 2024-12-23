from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
n= 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text = "Timer")
    check_mark.config(text = "✔")
    reps = 0
    canvas.itemconfig(timer_text, text = "00:00")



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_min = WORK_MIN * 60
    short_min = SHORT_BREAK_MIN *60
    long_min = LONG_BREAK_MIN
    reps +=1
    if reps %8 ==0:
        count_down(long_min)
        timer_label.config(text = "Break")

    elif reps % 2 == 0:
        count_down(short_min)
        timer_label.config(text = "Break")

    else:
        count_down(work_min)
        timer_label.config(text = "Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count /60)
    count_sec = count % 60
    if count_min < 10:
        count_min =f"0{count_min}"
    if count_sec < 10:
        count_sec =f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count >0:
        timer = window.after(1,count_down, count-1)

    else:
        start_timer()
        mark = ""
        for _ in range(int(reps/2)):
            mark += "✔"
        check_mark.config(text = mark)

def pause():
    window.after_cancel(timer)

def play():
    current_time = (canvas.itemcget(timer_text, 'text'))
    mins = current_time[0]+current_time[1]
    secs = current_time[3]+current_time[4]

    mins_to_secs = int(mins) *60
    count = int(secs) + int(mins_to_secs)
    window.after(1, count_down, int(count)-1)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx = 100,pady=50,bg = YELLOW)
window.minsize(600,500)




canvas = Canvas(width = 240, height = 224,bg = YELLOW, highlightthickness=0)
tomato_img= PhotoImage(file = "tomato.png")
canvas.create_image(123,112, image = tomato_img)
timer_text = canvas.create_text(123,130,text = "00:00", font = (FONT_NAME,35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text = "Start", command = start_timer)
start_button.grid(row=2, column=0)

timer_label = Label(text = "Timer", font = (FONT_NAME, 50), fg= GREEN, bg = YELLOW)
timer_label.grid(row=0,column=1)


reset_button = Button(text = "Reset", command = reset_timer)
reset_button.grid(row=2, column=2)

check_mark = Label(text="✔", fg = GREEN, bg = YELLOW)
check_mark.grid(row=3,column=1)

pause_button = Button(text = "Pause", command = pause)
pause_button.grid(column=1, row=4)

play_button = Button(text = "Play", command = play)
play_button.grid(column=1, row= 5)






window.mainloop()