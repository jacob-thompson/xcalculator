from tkinter import mainloop, Tk

from .calculator import Calculator

def main():
    print("easy-calculator https://github.com/jacob-thompson/easy-calculator")

    root = Tk()
    Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()