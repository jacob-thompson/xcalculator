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

        values = "eans0123456789.+-*/() "
        self.permitted_values = set(values)

        self.result_flag = False
        self.ans_flag = False

        self.problem = StringVar()
        self.result = StringVar()
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

        self.problem.trace_add("write", self.check)

        self.prob_entry.focus()

        self.root.bind("<BackSpace>", self.delete_digit)
        self.root.bind("<Escape>", self.clear_problem)

        self.root.bind("<KP_Add>", self.operand_addition)
        self.root.bind("+", self.operand_addition)

        self.root.bind("<KP_Subtract>", self.operand_subtraction)
        self.root.bind("-", self.operand_subtraction)

        self.root.bind("<KP_Multiply>", self.operand_multiplication)
        self.root.bind("*", self.operand_multiplication)

        self.root.bind("<KP_Divide>", self.operand_division)
        self.root.bind("/", self.operand_division)

        self.root.bind("(", self.append_open_paranthesis)
        self.root.bind(")", self.append_closed_paranthesis)

        self.root.bind("<KP_Decimal>", self.append_decimal)
        self.root.bind(".", self.append_decimal)

        self.root.bind("<KP_0>", self.append_zero)
        self.root.bind("0", self.append_zero)

        self.root.bind("<KP_1>", self.append_one)
        self.root.bind("1", self.append_one)

        self.root.bind("<KP_2>", self.append_two)
        self.root.bind("2", self.append_two)

        self.root.bind("<KP_3>", self.append_three)
        self.root.bind("3", self.append_three)

        self.root.bind("<KP_4>", self.append_four)
        self.root.bind("4", self.append_four)

        self.root.bind("<KP_5>", self.append_five)
        self.root.bind("5", self.append_five)

        self.root.bind("<KP_6>", self.append_six)
        self.root.bind("6", self.append_six)

        self.root.bind("<KP_7>", self.append_seven)
        self.root.bind("7", self.append_seven)

        self.root.bind("<KP_8>", self.append_eight)
        self.root.bind("8", self.append_eight)

        self.root.bind("<KP_9>", self.append_nine)
        self.root.bind("9", self.append_nine)

        self.root.bind("<KP_Enter>", self.calculate)
        self.root.bind("<KP_Equal>", self.calculate)
        self.root.bind("<Return>", self.calculate)
        self.root.bind("=", self.calculate)

        self.root.mainloop()

    def operand_addition(self, *args):
        if self.ans_flag:
            self.prob_entry.icursor(END)
            self.ans_flag = False

        if self.prob_entry.focus_get() == self.prob_entry:
            return

        operand = "+"
        current = self.problem.get()
        self.problem.set(current + operand)

    def operand_subtraction(self, *args):
        if self.ans_flag:
            self.prob_entry.icursor(END)
            self.ans_flag = False

        if self.prob_entry.focus_get() == self.prob_entry:
            return

        operand = "-"
        current = self.problem.get()
        self.problem.set(current + operand)

    def operand_multiplication(self, *args):
        if self.ans_flag:
            self.prob_entry.icursor(END)
            self.ans_flag = False

        if self.prob_entry.focus_get() == self.prob_entry:
            return

        operand = "*"
        current = self.problem.get()
        self.problem.set(current + operand)

    def operand_division(self, *args):
        if self.ans_flag:
            self.prob_entry.icursor(END)
            self.ans_flag = False

        if self.prob_entry.focus_get() == self.prob_entry:
            return

        operand = "/"
        current = self.problem.get()
        self.problem.set(current + operand)

    def append_closed_paranthesis(self, *args):
        if self.prob_entry.focus_get() == self.prob_entry:
            return

        paranthesis = ")"
        current = self.problem.get()
        self.problem.set(current + paranthesis)

    def append_open_paranthesis(self, *args):
        if self.prob_entry.focus_get() == self.prob_entry:
            return

        paranthesis = "("
        current = self.problem.get()
        self.problem.set(current + paranthesis)

    def append_decimal(self, *args):
        if self.prob_entry.focus_get() == self.prob_entry:
            return

        decimal = "."
        current = self.problem.get()
        self.problem.set(current + decimal)

    def append_zero(self, *args):
        if self.prob_entry.focus_get() == self.prob_entry:
            return

        zero = "0"
        current = self.problem.get()
        self.problem.set(current + zero)

    def append_one(self, *args):
        if self.prob_entry.focus_get() == self.prob_entry:
            return

        one = "1"
        current = self.problem.get()
        self.problem.set(current + one)

    def append_two(self, *args):
        if self.prob_entry.focus_get() == self.prob_entry:
            return

        two = "2"
        current = self.problem.get()
        self.problem.set(current + two)

    def append_three(self, *args):
        if self.prob_entry.focus_get() == self.prob_entry:
            return

        three = "3"
        current = self.problem.get()
        self.problem.set(current + three)

    def append_four(self, *args):
        if self.prob_entry.focus_get() == self.prob_entry:
            return

        four = "4"
        current = self.problem.get()
        self.problem.set(current + four)

    def append_five(self, *args):
        if self.prob_entry.focus_get() == self.prob_entry:
            return

        five = "5"
        current = self.problem.get()
        self.problem.set(current + five)

    def append_six(self, *args):
        if self.prob_entry.focus_get() == self.prob_entry:
            return

        six = "6"
        current = self.problem.get()
        self.problem.set(current + six)

    def append_seven(self, *args):
        if self.prob_entry.focus_get() == self.prob_entry:
            return

        seven = "7"
        current = self.problem.get()
        self.problem.set(current + seven)

    def append_eight(self, *args):
        if self.prob_entry.focus_get() == self.prob_entry:
            return

        eight = "8"
        current = self.problem.get()
        self.problem.set(current + eight)

    def append_nine(self, *args):
        if self.prob_entry.focus_get() == self.prob_entry:
            return

        nine = "9"
        current = self.problem.get()
        self.problem.set(current + nine)

    def calculate(self, *args):
        if self.problem.get() == "":
            return

        try:
            expression = sympify(self.problem.get())
        except SympifyError as err:
            print("Sympify error has occurred:", file=stderr)
            print(str(err), file=stderr)
            self.clear_problem()

        if "ans" in str(expression):
            value = expression.subs("ans", self.result.get())
            self.result.set(self.decimal_conversion(value))
            self.problem.set(self.result.get())
        else:
            self.result.set(self.decimal_conversion(expression))
            self.problem.set(self.result.get())

        self.result_flag = True
        self.prob_entry.icursor(END)

    def callback(self, entry):
        if set(entry).issubset(self.permitted_values) or entry == "":
            return True
        else:
            return False

    def check(self, *args):
        if self.result_flag:
            self.remove_result_from_entry()

        entry = self.problem.get()
        operands = list("+-*/")
        if entry in operands and self.result_flag:
            new_entry = "ans" + entry
            self.problem.set(new_entry)
            self.ans_flag = True

        self.result_flag = False

    def clear_problem(self, *args):
        self.problem.set("")

    def decimal_conversion(self, value):
        if "/" not in str(value) and "." not in str(value):
            return str(value)
        elif "." in str(value):
            return format(float(value), "g")
        else:
            return format(float(value.evalf()), "g")

    def delete_digit(self, *args):
        if self.prob_entry.focus_get() == self.prob_entry:
            return

        current = self.problem.get()
        self.problem.set(current[:-1])

    def remove_result_from_entry(self):
        result = self.result.get()
        entry = self.problem.get()

        for digit in list(result):
            entry = entry.replace(digit, "")

        self.problem.set(entry)