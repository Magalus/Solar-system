from math import sqrt
import random

class Create_planet:

    def __init__(self, color, size, distance, speed, canvas):
        self.color = color
        self.size = size
        self.distance = distance
        self.speed = speed
        self.x1, self.x2, self.y1, self.y2 = self.create_coords()
        self.move_x, self.move_y = self.create_move()
        self.canvas = canvas
        self.planet = self.create_planet_on_canvas()


    def create_coords(self):
        x1 = 1000/2 - round(sqrt(self.distance) * 8) - round(sqrt(sqrt(self.size)))
        y1 = 1000/2 - round(sqrt(self.distance) * 8) + round(sqrt(sqrt(self.size)))
        x2 = 1000/2 - round(sqrt(sqrt(self.size)))
        y2 = 1000/2 + round(sqrt(sqrt(self.size)))
        return x1, x2, y1, y2

    def create_move(self):
        move_x = random.randint(5, 15)
        move_y = random.randint(5, 15)
        return move_x, move_y

    def create_planet_on_canvas(self):
        planet = self.canvas.create_oval(self.x1, self.x2, self.y1, self.y2, fill=self.color)
        return planet
