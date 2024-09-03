from tkinter import *
from tkinter import ttk

class Calculator:

    def __init__(self, root):

        root.title("Calculator")
        root.geometry("175x250")
        root.minsize(125, 210)

        mainframe = ttk.Frame(root, borderwidth=3, relief="ridge", padding=("3 10 3 10"))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # configure 4x5 grid
        ## row 1
        ### input
        self.problem = StringVar()
        prob_entry = ttk.Entry(mainframe, textvariable=self.problem)
        prob_entry.grid(column=1, row=1, columnspan=4, sticky=(N, W, E))

        ## row 2
        ttk.Button(mainframe, text="÷", command=self.operand_division).grid(column=4, row=2, sticky=(W, E, S))
        ttk.Button(mainframe, text="9", command=self.append_nine).grid(column=3, row=2, sticky=(W, E, S))
        ttk.Button(mainframe, text="8", command=self.append_eight).grid(column=2, row=2, sticky=(W, E, S))
        ttk.Button(mainframe, text="7", command=self.append_seven).grid(column=1, row=2, sticky=(W, E, S))

        ## row 3
        ttk.Button(mainframe, text="×", command=self.operand_multiplication).grid(column=4, row=3, sticky=(W, E, S))
        ttk.Button(mainframe, text="6", command=self.append_six).grid(column=3, row=3, sticky=(W, E, S))
        ttk.Button(mainframe, text="5", command=self.append_five).grid(column=2, row=3, sticky=(W, E, S))
        ttk.Button(mainframe, text="4", command=self.append_four).grid(column=1, row=3, sticky=(W, E, S))

        ## row 4
        ttk.Button(mainframe, text="-", command=self.operand_subtraction).grid(column=4, row=4, sticky=(W, E, S))
        ttk.Button(mainframe, text="3", command=self.append_three).grid(column=3, row=4, sticky=(W, E, S))
        ttk.Button(mainframe, text="2", command=self.append_two).grid(column=2, row=4, sticky=(W, E, S))
        ttk.Button(mainframe, text="1", command=self.append_one).grid(column=1, row=4, sticky=(W, E, S))

        ## row 5
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

        prob_entry.focus() # set cursor to input

        root.bind("<Return>", self.calculate)

    def operand_addition(self, *args):
        operand = "+"
        current = self.problem.get()
        self.problem.set(current + operand)

    def operand_subtraction(self, *args):
        operand = "-"
        current = self.problem.get()
        self.problem.set(current + operand)

    def operand_multiplication(self, *args):
        operand = "*"
        current = self.problem.get()
        self.problem.set(current + operand)

    def operand_division(self, *args):
        operand = "/"
        current = self.problem.get()
        self.problem.set(current + operand)

    def append_decimal(self, *args):
        decimal = "."
        current = self.problem.get()
        self.problem.set(current + decimal)

    def append_zero(self, *args):
        zero = "0"
        current = self.problem.get()
        self.problem.set(current + zero)

    def append_one(self, *args):
        one = "1"
        current = self.problem.get()
        self.problem.set(current + one)

    def append_two(self, *args):
        two = "2"
        current = self.problem.get()
        self.problem.set(current + two)

    def append_three(self, *args):
        three = "3"
        current = self.problem.get()
        self.problem.set(current + three)

    def append_four(self, *args):
        four = "4"
        current = self.problem.get()
        self.problem.set(current + four)

    def append_five(self, *args):
        five = "5"
        current = self.problem.get()
        self.problem.set(current + five)

    def append_six(self, *args):
        six = "6"
        current = self.problem.get()
        self.problem.set(current + six)

    def append_seven(self, *args):
        seven = "7"
        current = self.problem.get()
        self.problem.set(current + seven)

    def append_eight(self, *args):
        eight = "8"
        current = self.problem.get()
        self.problem.set(current + eight)

    def append_nine(self, *args):
        nine = "9"
        current = self.problem.get()
        self.problem.set(current + nine)

    def calculate(self, *args):
        # placeholder
        try:
            value = float(self.problem.get())
            self.problem.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass