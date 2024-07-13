import tkinter as tk
from tkinter import messagebox
import random

class MemoryGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Emoji Memory Game")
        
        self.symbols = ['🍕', '🍔', '🌭', '🍿', '🍩', '🍦', '🍺', '🍷']
        self.symbols *= 2
        random.shuffle(self.symbols)
        
        self.size = 4
        self.buttons = []
        self.revealed = []
        self.first_choice = None
        self.pairs_found = 0
        
        self.create_board()
    
    def create_board(self):
        for i in range(self.size):
            row = []
            revealed_row = []
            for j in range(self.size):
                button = tk.Button(self.master, text='', width=5, height=2, 
                                   command=lambda x=i, y=j: self.on_click(x, y))
                button.grid(row=i, column=j, padx=2, pady=2)
                row.append(button)
                revealed_row.append(False)
            self.buttons.append(row)
            self.revealed.append(revealed_row)
    
    def on_click(self, row, col):
        if self.revealed[row][col]:
            return
        
        self.buttons[row][col].config(text=self.symbols[row*self.size + col])
        self.revealed[row][col] = True
        
        if self.first_choice is None:
            self.first_choice = (row, col)
        else:
            r1, c1 = self.first_choice
            if self.symbols[r1*self.size + c1] == self.symbols[row*self.size + col]:
                self.pairs_found += 1
                if self.pairs_found == len(self.symbols) // 2:
                    messagebox.showinfo("Congratulations!", "You've found all the pairs! 🏆")
            else:
                self.master.after(1000, self.hide_buttons, r1, c1, row, col)
            self.first_choice = None
    
    def hide_buttons(self, r1, c1, r2, c2):
        self.buttons[r1][c1].config(text='')
        self.buttons[r2][c2].config(text='')
        self.revealed[r1][c1] = False
        self.revealed[r2][c2] = False

root = tk.Tk()
game = MemoryGame(root)
root.mainloop()