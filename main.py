from tkinter import *
import time
from create_planet import Create_planet
from create_sun import Create_sun


def create_window():
    gui =Tk()
    gui.geometry('1000x1000')
    gui.title('Solar System')
    canvas = Canvas(gui, width=1000, height=1000, bg='black')
    canvas.pack()
    return gui, canvas


if __name__ == '__main__':
    gui, canvas = create_window()

    sun = Create_sun("yellow", 1391900, 200, 75000, canvas)
    # mercury = Create_planet("white", 4800, 58, 175936, canvas)
    # venus = Create_planet("green", 12000, 108, 126062, canvas)
    earth = Create_planet("blue", 12750, 149, 107243, canvas)
    # mars = Create_planet("red", 6800, 227, 87226, canvas)
    # jupiter = Create_planet("cyan", 142984, 778, 47196, canvas)
    saturn = Create_planet("magenta", 120536, 1434, 34962, canvas)
    # uranus = Create_planet("orange", 51312, 2871, 24459, canvas)
    # neptune = Create_planet("pink", 49922, 4495, 19566, canvas)

    while True:

        for planet in [earth, saturn]:
            canvas.move(planet.planet, planet.move_x, planet.move_y)
            pos = canvas.coords(planet.planet)
            if pos[3] >= 1000 or pos[1] <= 0:
                planet.move_x = -planet.move_x
            if pos[2] >= 1000 or pos[0] <0:
                planet.move_y = -planet.move_y
            gui.update()
            time.sleep(.1)

    gui.mainloop()
