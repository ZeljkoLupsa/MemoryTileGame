import tkinter as tk
import random
from tkinter import messagebox
import time
 
class MemoryTile:
    def __init__(self, roditelj):
        self.roditelj = roditelj
        self.buttons = [[tk.Button(root,
                                   width=4,
                                   height=2,
                                   command=lambda row=row, column=column: self.izaberi_polje(row, column)
                                   ) for column in range(4)] for row in range(4)]
        for row in range(4):
            for column in range(4):
                self.buttons[row][column].grid(row=row, column=column)
        self.first = None
        self.nacrtaj_tablu()
        
    def nacrtaj_tablu(self):
        self.odgovor = list('AABBCCDDEEFFGGHH')
        random.shuffle(self.odgovor)
        self.odgovor = [self.odgovor[:4],
                       self.odgovor[4:8],
                       self.odgovor[8:12],
                       self.odgovor[12:]]
        for row in self.buttons:
            for button in row:
                button.config(text='', state=tk.NORMAL)
        self.start_time = time.monotonic()
                       
    def izaberi_polje(self, row, column):
        self.buttons[row][column].config(text=self.odgovor[row][column])
        self.buttons[row][column].config(state=tk.DISABLED)
        if not self.first:
            self.first = (row, column)
        else:
            a,b = self.first
            if self.odgovor[row][column] == self.odgovor[a][b]:
                self.odgovor[row][column] = ''
                self.odgovor[a][b] = ''
                if not any(''.join(row) for row in self.odgovor):
                    duration = time.monotonic() - self.start_time
                    messagebox.showinfo(title='Uspjesno!', message='Vi ste pobjednik! Time: {:.1f}'.format(duration))
                    self.roditelj.after(5000, self.nacrtaj_tablu)
            else:
                self.roditelj.after(3000, self.sakrij_polje, row, column, a, b)
            self.first = None
    
    def sakrij_polje(self, x1, y1, x2, y2):
        self.buttons[x1][y1].config(text='', state=tk.NORMAL)
        self.buttons[x2][y2].config(text='', state=tk.NORMAL)
 
root = tk.Tk()
memory_tile = MemoryTile(root)
root.mainloop()
 
 
 
 
 
 

