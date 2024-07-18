import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.entry = tk.Entry(root, width=25, font=('Helvetica', 14), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, width=5, height=2, font=('Helvetica', 12),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)
        
        clear_button = tk.Button(root, text='C', width=5, height=2, font=('Helvetica', 12),
                                 command=self.clear_entry)
        clear_button.grid(row=5, column=0, columnspan=3, padx=5, pady=5)
        
        exit_button = tk.Button(root, text='Exit', width=5, height=2, font=('Helvetica', 12),
                                command=root.quit)
        exit_button.grid(row=5, column=3, padx=5, pady=5)
    
    def on_button_click(self, char):
        current_text = self.entry.get()
        
        if char == '=':
            try:
                result = eval(current_text)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, char)
    
    def clear_entry(self):
        self.entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
