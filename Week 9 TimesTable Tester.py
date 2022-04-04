from tkinter import *
import random


class Tester:
    def __init__(self, parent):
        self.num = Label(parent, text="Click Next to start", padx=10, pady=2)

        self.num.grid(row=1, column=1)

        self.ans = Entry(parent, width=5)
        self.ans.grid(row=1, column=2, padx=10, pady=2)

        self.check = Button(parent, text="Check Answer",
                            padx=3, pady=2, bd=1, bg="#4CAF50", command=self.check_answer)
        self.check.grid(row=2, column=1, padx=3, pady=2)

        self.next = Button(parent, text="Next", padx=3,
                           pady=2, bd=1, bg="#008CBA", command=self.next_question)
        self.next.grid(row=2, column=2)

        self.answer = Label(parent, text="")
        self.answer.grid(row=3, column=1, columnspan=2)

    def next_question(self):
        global i
        self.x = random.randint(1, 10)
        for i in range(1, 10):
            self.num.config(text=f"{i} x {self.x} = ")

    def check_answer(self):
        try:
            self.f = float(self.ans.get())
            if self.f == i * self.x:
                self.answer.config(text="Yor are SMART!", bg="Yellow")
            else:
                self.answer.config(text="You got it wrong.", bg="Red")
        except:
            self.answer.config(text="Improper Input", bg="Red")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Times Table Tester")
    root.geometry("190x100")

    test = Tester(root)
    root.mainloop()
