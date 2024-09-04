from sys import stderr
from tkinter import *
from tkinter import ttk

from sympy import sympify, SympifyError

class Calculator:

    def __init__(self):
        self.root = Tk()
        self.root.title("xcalculator")
        self.root.geometry("250x325")
        self.root.minsize(125, 210)

        mainframe = ttk.Frame(self.root, borderwidth=2, relief="ridge", padding=("3 10 3 10"))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        values = "0123456789.+-*/() "
        self.permitted_values = set(values)

        self.problem = StringVar()
        vcmd = (mainframe.register(self.callback))
        self.prob_entry = ttk.Entry(mainframe, textvariable=self.problem, validate="all", validatecommand=(vcmd, "%P"))
        self.prob_entry.grid(column=1, row=1, columnspan=4, sticky=(N, W, E))

        ttk.Button(mainframe, text="÷", command=self.operand_division).grid(column=4, row=2, sticky=(W, E, S))
        ttk.Button(mainframe, text="9", command=self.append_nine).grid(column=3, row=2, sticky=(W, E, S))
        ttk.Button(mainframe, text="8", command=self.append_eight).grid(column=2, row=2, sticky=(W, E, S))
        ttk.Button(mainframe, text="7", command=self.append_seven).grid(column=1, row=2, sticky=(W, E, S))

        ttk.Button(mainframe, text="×", command=self.operand_multiplication).grid(column=4, row=3, sticky=(W, E, S))
        ttk.Button(mainframe, text="6", command=self.append_six).grid(column=3, row=3, sticky=(W, E, S))
        ttk.Button(mainframe, text="5", command=self.append_five).grid(column=2, row=3, sticky=(W, E, S))
        ttk.Button(mainframe, text="4", command=self.append_four).grid(column=1, row=3, sticky=(W, E, S))

        ttk.Button(mainframe, text="-", command=self.operand_subtraction).grid(column=4, row=4, sticky=(W, E, S))
        ttk.Button(mainframe, text="3", command=self.append_three).grid(column=3, row=4, sticky=(W, E, S))
        ttk.Button(mainframe, text="2", command=self.append_two).grid(column=2, row=4, sticky=(W, E, S))
        ttk.Button(mainframe, text="1", command=self.append_one).grid(column=1, row=4, sticky=(W, E, S))

        ttk.Button(mainframe, text="+", command=self.operand_addition).grid(column=4, row=5, sticky=(W, E, S))
        ttk.Button(mainframe, text="=", command=self.calculate).grid(column=3, row=5, sticky=(W, E, S))
        ttk.Button(mainframe, text=".", command=self.append_decimal).grid(column=2, row=5, sticky=(W, E, S))
        ttk.Button(mainframe, text="0", command=self.append_zero).grid(column=1, row=5, sticky=(W, E, S))

        mainframe.grid_columnconfigure(1, weight=1)
        mainframe.grid_columnconfigure(2, weight=1)
        mainframe.grid_columnconfigure(3, weight=1)
        mainframe.grid_columnconfigure(4, weight=1)
        mainframe.grid_rowconfigure(1, weight=1)
        mainframe.grid_rowconfigure(2, weight=1)
        mainframe.grid_rowconfigure(3, weight=1)
        mainframe.grid_rowconfigure(4, weight=1)
        mainframe.grid_rowconfigure(5, weight=1)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        self.prob_entry.focus()

        self.root.bind("<Return>", self.calculate)
        self.root.bind("<Escape>", self.clear_problem)

        self.root.mainloop()

    def operand_addition(self):
        operand = "+"
        current = self.problem.get()
        self.problem.set(current + operand)

    def operand_subtraction(self):
        operand = "-"
        current = self.problem.get()
        self.problem.set(current + operand)

    def operand_multiplication(self):
        operand = "*"
        current = self.problem.get()
        self.problem.set(current + operand)

    def operand_division(self):
        operand = "/"
        current = self.problem.get()
        self.problem.set(current + operand)

    def append_decimal(self):
        decimal = "."
        current = self.problem.get()
        self.problem.set(current + decimal)

    def append_zero(self):
        zero = "0"
        current = self.problem.get()
        self.problem.set(current + zero)

    def append_one(self):
        one = "1"
        current = self.problem.get()
        self.problem.set(current + one)

    def append_two(self):
        two = "2"
        current = self.problem.get()
        self.problem.set(current + two)

    def append_three(self):
        three = "3"
        current = self.problem.get()
        self.problem.set(current + three)

    def append_four(self):
        four = "4"
        current = self.problem.get()
        self.problem.set(current + four)

    def append_five(self):
        five = "5"
        current = self.problem.get()
        self.problem.set(current + five)

    def append_six(self):
        six = "6"
        current = self.problem.get()
        self.problem.set(current + six)

    def append_seven(self):
        seven = "7"
        current = self.problem.get()
        self.problem.set(current + seven)

    def append_eight(self):
        eight = "8"
        current = self.problem.get()
        self.problem.set(current + eight)

    def append_nine(self):
        nine = "9"
        current = self.problem.get()
        self.problem.set(current + nine)

    def calculate(self, *args):
        if self.problem.get() == "":
            return

        try:
            value = sympify(self.problem.get(), evaluate=True)
            result = self.decimal_conversion(value)
            self.problem.set(result)
        except SympifyError as err:
            print("Sympify error has occurred:", file=stderr)
            print(str(err), file=stderr)
            self.clear_problem()

        self.prob_entry.icursor(END)

    def callback(self, entry):
        if set(entry).issubset(self.permitted_values) or entry == "":
            return True
        else:
            return False

    def clear_problem(self, *args):
        self.problem.set("")

    def decimal_conversion(self, value):
        if "/" not in str(value) and "." not in str(value):
            return str(value)
        elif "." in str(value):
            return format(float(value), "g")
        else:
            return format(float(value.evalf()), "g")