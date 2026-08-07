import tkinter as tk
from time import strftime

# setup the window
root = tk.Tk()
root.title("Window Clock")

# function that shows the current time.
def timefunc():
    vartime = strftime("%I:%M:%S %p")
    clock.config(text = vartime)
    clock.after(1000, timefunc)

clock = tk.Label(root, font=("helvetica", 60, "bold"), background="blue", foreground="white")
clock.pack(anchor="center") # aligning the clock to the middle

timefunc()

if __name__ == "__main__":
    root.mainloop()
