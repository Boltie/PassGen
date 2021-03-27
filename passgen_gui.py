from passgen import PassGen
from tkinter import *
from tkinter import ttk

def generate(args=None):
    global length
    if length.get() != "":
        enabled = ""
        enabled += ("1" if lower.get() else "0")
        enabled += ("1" if upper.get() else "0")
        enabled += ("1" if digit.get() else "0")
        enabled += ("1" if special.get() else "0")
        password_entry.configure(state="normal")
        password_entry.delete(0, "end")
        pw = pg.get_single(allow_repeats=repeats.get(), length=length.get(), sets_enabled=enabled)
        password_entry.insert(0, pw)
        password_entry.selection_range(0, "end")
        password_entry.focus_set()
        password_entry.configure(state="readonly")

pg = PassGen()
root = Tk()
root.resizable(0, 0)
root.title("PassGen")

mainframe = ttk.Frame(root)

generate_button = ttk.Button(mainframe, command=generate, text="Generate", width=9)

length_label = ttk.Label(mainframe, text="Length")
length = IntVar(value=16)
length_entry = ttk.Entry(mainframe, justify="center", textvariable=length, width=9)

lower = BooleanVar(value=True)
lower_check = ttk.Checkbutton(mainframe, text="Lower", variable=lower, onvalue=True)
upper = BooleanVar(value=True)
upper_check = ttk.Checkbutton(mainframe, text="Upper", variable=upper, onvalue=True)
digit = BooleanVar(value=True)
digit_check = ttk.Checkbutton(mainframe, text="Digit", variable=digit, onvalue=True)
special = BooleanVar(value=True)
special_check = ttk.Checkbutton(mainframe, text="Special", variable=special, onvalue=True)
repeats = BooleanVar(value=False)
repeats_check = ttk.Checkbutton(mainframe, text="Repeats", variable=repeats, onvalue=True)

password = StringVar(value="")
password_entry = ttk.Entry(mainframe, justify="center", textvariable=password)

mainframe.grid(column=0, row=0)
lower_check.grid(column=0, row=0, sticky=W)
upper_check.grid(column=1, row=0, sticky=W+E)
length_label.grid(column=2, row=0, sticky=E)
length_entry.grid(column=3, row=0, sticky=W+E)
digit_check.grid(column=0, row=1, sticky=W)
special_check.grid(column=1, row=1, sticky=W+E)
repeats_check.grid(column=2, row=1, sticky=E)
generate_button.grid(column=3, row=1, sticky=E)
password_entry.grid(column=0, row=2, columnspan=4, sticky=W+E)

password_entry.configure(state="readonly")

root.bind("<Return>", generate)

root.mainloop()