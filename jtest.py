
from tkinter import *

my_font = ("Arial", 17, "bold")
current_font = ("Arial", 45, "bold")

class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("My Calculator")
        
        self.total_label, self.current_label = self.display()
        self.total_display = "0"
        self.current_display = "0"
        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_button_frame()
        
    def display(self):
        total_label = Label(self.display_frame, text=self.total_display, anchor=E, bg="gray", font=my_font, padx=24)
        total_label.pack(expand=True, fill="both")
        
        current_label = Label(self.button_frame, text=self.current_display, anchor=E, bg="white", font=current_font, padx=24)
        current_label.pack(expand=True, fill="both")
        
        return total_label, current_label
        
    def create_display_frame(self):
        frame = Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    
    def create_button_frame(self):
        frame = Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
        

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    cal = Calculator()
    cal.run()

