from math import sqrt

class Create_sun:

    def __init__(self, color, size , canvas):
        self.color = color
        self.size = size
        self.x1, self.x2, self.y1, self.y2 = self.create_coords()
        self.canvas = canvas
        self.sun = self.create_sun_on_canvas()

    def create_coords(self):
        x1 = 900/2 - self.size
        y1 = 900/2 + self.size
        x2 = 900/2 - self.size
        y2 = 900/2 + self.size
        return x1, x2, y1, y2

    def create_sun_on_canvas(self):
        sun = self.canvas.create_oval(self.x1, self.x2, self.y1, self.y2, fill=self.color)
        return sun