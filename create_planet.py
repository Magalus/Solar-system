import math
import copy

class Create_planet:

    def __init__(self, color, size, distance, speed, canvas):
        self.color = color
        self.size = size
        self.distance = distance
        self.speed = speed
        self.x1, self.y1, self.x2, self.y2 = self.create_coords()
        self.move_x = 1
        self.move_y = 1
        self.canvas = canvas
        self.planet = self.create_planet_on_canvas()
        self.limit = self.distance + round(self.size/2)

    def create_coords(self):
        x1 = 900/2 - self.distance - round(self.size/2)
        y1 = 900/2 - self.distance + round(self.size/2)
        x2 = 900/2 - round(self.size/2)
        y2 = 900/2 + round(self.size/2)
        return x1, y1, x2, y2

    def update_move(self, pos):
        pos_x = pos[0] + round((pos[2]-pos[0])/2)
        pos_y = pos[1] + round((pos[3]-pos[1])/2)
        dist = self.calculateDistance(pos_x, pos_y, 450, 450)
        if pos_x < 450 and pos_y < 450 and dist < self.limit:
            self.move_x = -1
            self.move_y = 0
        elif pos_x < 450 and pos_y < 450 and dist > self.limit:
            self.move_x = -1
            self.move_y = 1
        elif pos_x < 450 and pos_y > 450 and dist < self.limit:
            self.move_x = 0
            self.move_y = 1
        elif pos_x < 450 and pos_y > 450 and dist > self.limit:
            self.move_x = 1
            self.move_y = 1
        elif pos_x > 450 and pos_y > 450 and dist < self.limit:
            self.move_x = 1
            self.move_y = 0
        elif pos_x < 450 and pos_y > 450 and dist > self.limit:
            self.move_x = 1
            self.move_y = -1
        elif pos_x > 450 and pos_y < 450 and dist < self.limit:
            self.move_x = 0
            self.move_y = -1
        elif pos_x < 450 and pos_y < 450 and dist > self.limit:
            self.move_x = -1
            self.move_y = -1

        print(pos_x, pos_y, dist, self.limit)


    def create_planet_on_canvas(self):
        planet = self.canvas.create_oval(self.x1, self.x2, self.y1, self.y2, fill=self.color)
        return planet

    def calculateDistance(self, x1, y1, x2, y2):
        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return round(dist)