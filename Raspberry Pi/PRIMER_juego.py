# Modificado por Daniel Rodas Flores
from sense_hat import SenseHat
import time


s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
maroon = (128,0,0)
def trinket_logo():
    G = green
    Y = yellow
    B = blue
    O = nothing
    M = maroon
    R = red
    P = pink
    logo = [
    O, O, P, O, P, O, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, R, O, R, O, O,
    R, R, R, R, R, R, O, O,
    O, O, O, R, O, O, O, O,
    O, O, M, M, M, O, O, O,
    O, B, M, O, M, O, O, O,
    O, O, B, O, B, B, O, O,
    ]
    return logo

def trinket_logo1():
    G = green
    Y = yellow
    B = blue
    O = nothing
    M = maroon
    R = red
    P = pink
    logo = [
    O, O, P, Y, P, O, O, O,
    O, O, P, P, P, O, O, O,
    O, R, O, R, O, O, O, O,
    O, R, R, R, R, R, R, O,
    O, O, O, R, O, O, O, O,
    O, O, M, M, M, O, O, O,
    O, O, M, O, M, B, O, O,
    O, B, B, O, B, O, O, O,
    ]
    return logo


images = [trinket_logo, trinket_logo1]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
