from tkinter import *

class CanvasWrapper:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Eraser Canvas")
        self.canvas = Canvas(self.root, width=width, height=height, bg="white")
        self.canvas.pack()
        self.root.update()

    def create_rectangle(self, x1, y1, x2, y2, color):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)

    def moveto(self, obj, x, y):
        self.canvas.coords(obj, x, y, x+20, y+20)  # Adjust for eraser size

    def get_mouse_x(self):
        return self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()

    def get_mouse_y(self):
        return self.canvas.winfo_pointery() - self.canvas.winfo_rooty()

    def find_overlapping(self, x1, y1, x2, y2):
        return self.canvas.find_overlapping(x1, y1, x2, y2)

    def run(self):
        self.root.mainloop()
