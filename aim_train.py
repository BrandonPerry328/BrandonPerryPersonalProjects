import tkinter as tk

window = tk.Tk(className="Aim Trainer")

# window.geometry("700x600")

program = tk.Canvas(window, bg="black", height="600", width="700")
# x0, y0, x1, y1
# max x = 700, max y = 600
oval = program.create_oval(0, 0, 50, 50, fill="white")
oval = program.create_oval(650, 550, 700, 600, fill="white")
program.pack()
window.mainloop()