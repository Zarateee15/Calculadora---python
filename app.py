import tkinter as tk
import random

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")  
        self.resizable(False,False) 
        self.geometry("320x450")  
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, bg="white", font=("Helvetica", 20))
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), (',', 4, 1), ('=', 4, 2), ('/', 4, 3),
            ('C', 5, 0, 4)
        ]
        
        for button in buttons:
            if len(button) == 4:
                text, row, col, colspan = button
            else:
                text, row, col = button
                colspan = 1
                
            button = tk.Button(self, text = text, font=("Helvetica", 20), command= lambda t=text: self.button_action(t))
            button.grid(row=row, column=col, columnspan=colspan, sticky="nsew")
            
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
            

    def button_action(self, char):
        if char == "=":
            expresion = self.display.get()
            try:
                result = eval(expresion.replace(',', '.'))
            except Exception as e:
                result = "Error"
                
            self.display.delete(0,tk.END)
            self.display.insert(tk.END, result)
        elif char == "C":
            self.display.delete(0,tk.END)
        else:   
            self.display.insert(tk.END, char)
            

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()



