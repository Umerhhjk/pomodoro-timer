import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
reps = 0
timer: str | None = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_button_pressed():
    Window.after_cancel(timer)
    timer_label.config(text="Timer")
    check_mark.config(text=CHECKMARK)
    image_canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_button_pressed():
    global reps
    reps = reps + 1
    if reps > 8:
        timer_label.config(text="That Is Enough \nFor Today")
        return

    if reps % 2 != 0:
        countdown(WORK_MIN * 60)
        timer_label.config(text="Working")
        check_mark.config(text="")
    elif reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break")
        check_mark.config(text=CHECKMARK)
    else:
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Short Break")
        check_mark.config(text=CHECKMARK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count_timer):
    minutes = int(count_timer // 60)
    seconds = int(count_timer % 60)
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"

    time_text = f"{minutes}:{seconds}"
    image_canvas.itemconfig(timer_text, text=time_text)
    if count_timer > 0:
        global timer
        timer = Window.after(1000, countdown, count_timer - 1)
    else:
        start_button_pressed()

# ---------------------------- UI SETUP ------------------------------- #

Window = tkinter.Tk()
Window.title("Pomodoro")
Window.config(bg=YELLOW, pady=50, padx=100)

timer_label = tkinter.Label(text="TIMER", bg= YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"), highlightthickness=0)
timer_label.grid(row=0, column=1)

start_button = tkinter.Button(text="Start", bg=YELLOW, highlightthickness=0, command= start_button_pressed)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_button_pressed)
reset_button.grid(row=2, column=2)

image_canvas = tkinter.Canvas(width=200, height=224)
image_canvas.config(bg=YELLOW, highlightthickness=0)
image = tkinter.PhotoImage(file="tomato.png")
image_canvas.create_image(100, 112, image=image)
timer_text = image_canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
image_canvas.grid(row=1, column=1)

check_mark = tkinter.Label(text=CHECKMARK, bg=YELLOW, fg=GREEN, highlightthickness=0, font=(FONT_NAME, 15, "bold"))
check_mark.grid(row=3, column=1)

Window.mainloop()