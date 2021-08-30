from tkinter import *
import time
from create_planet import Create_planet
from create_sun import Create_sun


def create_window():
    gui =Tk()
    gui.geometry('900x900')
    gui.title('Solar System')
    canvas = Canvas(gui, width=900, height=900, bg='black')
    canvas.pack()
    return gui, canvas


if __name__ == '__main__':
    gui, canvas = create_window()

    sun = Create_sun("yellow", 1391900, 200, 75000, canvas)
    mercury = Create_planet("white", 3, 60, 9, canvas)
    venus = Create_planet("green", 6, 70, 6, canvas)
    earth = Create_planet("blue", 6, 80, 5, canvas)
    mars = Create_planet("red", 3, 100, 4, canvas)
    jupiter = Create_planet("cyan", 20, 130, 3, canvas)
    saturn = Create_planet("magenta", 18, 180, 2, canvas)
    uranus = Create_planet("orange", 12, 290, 1, canvas)
    neptune = Create_planet("pink", 12, 420, 1, canvas)

    while True:
        for planet in [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]:
            for x in range(planet.speed):
                canvas.move(planet.planet, planet.move_x, planet.move_y)
                pos = canvas.coords(planet.planet)
                planet.update_move(pos)
                gui.update()
        time.sleep(.01)

    gui.mainloop()
