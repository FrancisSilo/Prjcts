import tkinter as tk

class Calculator:
    def __init__(self):
        # Creates the main window
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.expression = ""

        # Create the display entry widget
        self.display = tk.Entry(self.root, font=("Arial", 18), justify="center")
        self.display.grid(row=0, column=0, columnspan=4, padx=8, pady=8)

        # Calculator buttons from 0-9 and the operators
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        # Positions the buttons
        for i, button_text in enumerate(buttons):
            row, col = divmod(i, 4)
            button = tk.Button(self.root, text=button_text, font=("Arial", 12, "bold"), command=lambda text=button_text: self.on_button_click(text), bg="lightgray", fg="black")
            button.grid(row=row+1, column=col, padx=5, pady=5, ipadx=10, ipady=10)

        # Start the loop
        self.root.mainloop()

    def on_button_click(self, text):
        if text == "=":
            try:
                # Evaluate the expression and update the display
                self.expression = str(eval(self.expression))
            except ZeroDivisionError:
                self.expression = "Error: Division by zero"
            except Exception:
                self.expression = "Error: Invalid expression"
        elif text == "C":
            # Clear
            self.expression = ""
        else:
            self.expression += text

        # Update the display
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    Calculator()
