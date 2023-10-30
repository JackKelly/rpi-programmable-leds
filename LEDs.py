#!/usr/bin/env python
# coding: utf-8

from time import sleep

import board
import neopixel

TOTAL_NUM_LIGHTS = 150
PIN = board.D18

ARROW_START = 5
ARROW_HEAD_MIDDLE = 64
ARROW_END = 137

# Initialise pixels
pixels = neopixel.NeoPixel(PIN, TOTAL_NUM_LIGHTS, auto_write=False)
pixels.fill((0, 0, 0))
pixels.show()

# Handy functions
def fill_between(pixels, colour, start=ARROW_START, end=ARROW_END+1):
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
                fill_between(pixels, colour)
                pixels.show()
                

def animate_arrow():
    arrow_length = ARROW_HEAD_MIDDLE - ARROW_START
    for position in range(arrow_length):
        fill_between(pixels, (10, 1, 0))

        STEP = 20
        for repeat in range(2):
            offset = STEP * repeat
            
            # Light moving forwards:
            forwards_pos = ARROW_START + position + offset
            if forwards_pos < ARROW_HEAD_MIDDLE:
                pixels[forwards_pos] = (255, 0, 0)
    
            # Light moving "backwards":
            backwards_pos = ARROW_END - position - offset
            if backwards_pos > ARROW_HEAD_MIDDLE:
                pixels[backwards_pos] = (255, 0, 0)
        
        pixels.show()
        sleep(0.05)
        

def strobe(delay=0.05):
    for _ in range(20):
        fill_between(pixels, (255, 25, 0))# (40, 8, 0))
        pixels.show()
        sleep(delay)
        fill_between(pixels, (150, 0, 0))
        pixels.show()
        sleep(delay)


def colour_madness(delay=0.01):
    for _ in range(10):
        fill_between(pixels, (255, 0, 0))
        pixels.show()
        sleep(delay)
        fill_between(pixels, (0, 255, 0))
        pixels.show()
        sleep(delay)
        fill_between(pixels, (0, 0, 255))
        pixels.show()
        sleep(delay)

while True:
    up_and_down()
    animate_arrow()
    # strobe()
    # colour_madness()

