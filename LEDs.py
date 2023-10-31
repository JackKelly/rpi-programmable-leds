#!/usr/bin/env python
# coding: utf-8

from time import sleep

import board
import neopixel

# Constants about the hardware
TOTAL_NUM_LIGHTS = 150
PIN = board.D18

# Initialise pixels
pixels = neopixel.NeoPixel(PIN, TOTAL_NUM_LIGHTS, auto_write=False)
pixels.fill((0, 0, 0))
pixels.show()

def fill_list(colour, list_of_pixel_locations: list[int]):
    for position in list_of_pixel_locations:
        pixels[position] = colour

# Constants about the "trick or treat" sign:
START = 5
END = 137

# The lines are in order, from the top right to the bottom left:
ARROW_LINE_TOP_RIGHT = list(range(6, 12))
SIGN_RIGHT = list(range(12, 23))
SIGN_BOTTOM = list(range(23, 38)) + list(range(83, 88))
SIGN_LIGHT_BOTTOM = list(range(38, 43))
ARROW_LINE_BOTTOM_RIGHT = list(range(43, 50))
ARROW_HEAD_SHORT_BOTTOM = list(range(50, 54))
ARROW_HEAD_LONG_BOTTOM = list(range(54, 63))
ARROW_POINT = [63]
ARROW_HEAD_LONG_TOP = list(range(64, 73))[::-1]
ARROW_HEAD_SHORT_TOP = list(range(73, 78))
ARROW_LINE_BOTTOM_LEFT = list(range(78, 83))[::-1]
SIGN_LEFT = list(range(88, 99))[::-1]
SIGN_TOP = list(range(99, 121))
SIGN_LIGHT_TOP = list(range(121, 125))
ARROW_LINE_TOP_LEFT = list(range(130, 124, -1))
ARROW_TOP_END = list(range(131, 137)) + [5, 137]

ARROW_ALL = (
    ARROW_LINE_TOP_RIGHT + ARROW_LINE_BOTTOM_RIGHT + ARROW_HEAD_SHORT_BOTTOM +
    ARROW_HEAD_LONG_BOTTOM + ARROW_POINT + ARROW_HEAD_LONG_TOP + ARROW_HEAD_SHORT_TOP +
    ARROW_LINE_BOTTOM_LEFT + ARROW_LINE_TOP_LEFT + ARROW_TOP_END
)

SIGN_ALL = (
    SIGN_RIGHT + SIGN_BOTTOM + SIGN_LEFT + SIGN_TOP
)

# Colours
BACKGROUND_COLOUR = (10, 1, 0)
DOT_COLOUR = (255, 10, 0)

def test_lights():
    fill_list((0, 200, 0), ARROW_TOP_END)
    fill_list((0, 200, 100), ARROW_LINE_TOP_LEFT)
    fill_list((200, 100, 0), ARROW_LINE_TOP_RIGHT)
    fill_list((0, 0, 255), SIGN_RIGHT)
    fill_list((0, 255, 0), SIGN_BOTTOM)
    fill_list((255, 255, 255), SIGN_LIGHT_BOTTOM)
    fill_list((255, 0, 0), ARROW_LINE_BOTTOM_RIGHT)
    fill_list((0, 0, 255), ARROW_HEAD_SHORT_BOTTOM)
    fill_list((0, 255, 0), ARROW_HEAD_LONG_BOTTOM)
    fill_list((255, 0, 0), ARROW_POINT)
    fill_list((0, 255, 0), ARROW_HEAD_LONG_TOP)
    fill_list((0, 0, 255), ARROW_HEAD_SHORT_TOP)
    fill_list((255, 0, 255), ARROW_LINE_BOTTOM_LEFT)
    fill_list((255, 0, 0), SIGN_LEFT)
    fill_list((0, 255, 0), SIGN_TOP)
    fill_list((255, 255, 255), SIGN_LIGHT_TOP)
    pixels.show()

    
def animate_top_end_arrow(i: int, dot_colour):
    fill_list(dot_colour, ARROW_TOP_END[3-i:i+5])


def animate_arrow(i: int, dot_colour=DOT_COLOUR, background_colour=BACKGROUND_COLOUR):
    fill_list(background_colour, ARROW_ALL)
    if 0 <= i < 4:
        animate_top_end_arrow(i, dot_colour)
    elif 4 <= i < 10:
        new_i = i - 4
        for lst in [ARROW_LINE_TOP_LEFT, ARROW_LINE_TOP_RIGHT]:
            position = lst[new_i]
            pixels[position] = dot_colour
    # Leave 14 steps for the dot to go "behind" the sign
    elif 23 <= i < 30:
        position_bottom = ARROW_LINE_BOTTOM_RIGHT[i - 23]
        pixels[position_bottom] = dot_colour
        if 25 <= i:
            position_top = ARROW_LINE_BOTTOM_LEFT[i - 25]
            pixels[position_top] = dot_colour
    elif i == 30:
        fill_list(dot_colour, ARROW_HEAD_SHORT_BOTTOM + ARROW_HEAD_SHORT_TOP)
    elif 31 <= i < 40:
        new_i = i - 31
        position_top = ARROW_HEAD_LONG_TOP[new_i]
        position_bottom = ARROW_HEAD_LONG_BOTTOM[new_i]
        pixels[position_top] = dot_colour
        pixels[position_bottom] = dot_colour
    elif i == 40:
        pixels[ARROW_POINT[0]] = dot_colour

       
def animate_sign_border(i: int, dot_colour=DOT_COLOUR, background_colour=BACKGROUND_COLOUR):
    fill_list(background_colour, SIGN_ALL)
    if i == 10:
        fill_list(dot_colour, SIGN_TOP)
    if 11 <= i < 22:
        new_i = i - 11
        position_left = SIGN_LEFT[new_i]
        position_right = SIGN_RIGHT[new_i]
        pixels[position_left] = dot_colour
        pixels[position_right] = dot_colour
    if i == 22:
        fill_list(dot_colour, SIGN_BOTTOM)
        
def sign_flash(step: int = 2):
    for _ in range(7):
        for i in range(2):
            # SIGN:
            fill_list(BACKGROUND_COLOUR, SIGN_ALL)
            positions_a = SIGN_ALL[i::step]
            positions_b = SIGN_ALL[i+1::step]
            fill_list((255, 100, 0), positions_a)
            fill_list(DOT_COLOUR, positions_b)
            
            # ARROW:
            fill_list(BACKGROUND_COLOUR, ARROW_ALL)
            positions_a = ARROW_ALL[i::step]
            positions_b = ARROW_ALL[i+1::step]
            fill_list((0, 100, 255), positions_a)
            fill_list((255, 10, 0), positions_b)
            
            pixels.show()
            sleep(0.1)

def main():
    # Turn on the "sign lights":
    fill_list((255, 255, 255), SIGN_LIGHT_TOP + SIGN_LIGHT_BOTTOM)
    
    for i in range(0, 41):
        animate_arrow(i)
        animate_sign_border(i)
        pixels.show()
        sleep(0.05)

    sign_flash()

for _ in range(5):
    main()

# Handy functions
def fill_between(colour, start=START, end=END+1):
    for position in range(start, end):
        pixels[position] = colour

def up_and_down():
    MIN_BRIGHTNESS = 10
    MAX_BRIGHTNESS = 255
    for repeat in range(1):
        for direction in [
            range(MIN_BRIGHTNESS, MAX_BRIGHTNESS),
            range(MAX_BRIGHTNESS, MIN_BRIGHTNESS, -1)]:
            for i in direction:
                colour = (i, i * 0.1, 0)
                fill_between(colour)
                pixels.show()
        

def strobe(delay=0.05):
    for _ in range(20):
        fill_between((255, 25, 0))# (40, 8, 0))
        pixels.show()
        sleep(delay)
        fill_between((150, 0, 0))
        pixels.show()
        sleep(delay)


def colour_madness(delay=0.01):
    for _ in range(10):
        fill_between((255, 0, 0))
        pixels.show()
        sleep(delay)
        fill_between((0, 255, 0))
        pixels.show()
        sleep(delay)
        fill_between((0, 0, 255))
        pixels.show()
        sleep(delay)

#while True:
    # up_and_down()
    # animate_arrow()
    # strobe()
    # colour_madness()

