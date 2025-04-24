from tkinter import Button,Label
from tkinter.simpledialog import Dialog

class number_picker(Dialog):
    def __init__(self, parent, title, message, options):
        self.options = options
        self.result = 0
        super().__init__(parent, title)

    def body(self, master):
        Label(master, text="Select a number").grid(row=0, column=0, columnspan=3)
        for index, number in enumerate(self.options):
            button=Button(
                master, text=str(number),
                width=4, command=lambda n=number: self.set_result(n)
            )
            button.grid(row=(index // 3) + 1, column=index % 3, padx=5, pady=5)
        Button(master, text="Reset", command=lambda: self.set_result(0)).grid(row=4, column=0, columnspan=3, pady=10)
        return None

    def set_result(self, value):
        self.result = value
        self.destroy()