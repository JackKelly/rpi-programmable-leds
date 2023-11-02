## Programming LEDs from a Raspberry Pi

This code runs the "Trick or Treat" sign that we made for Halloween 2023.

See [this short video](https://photos.app.goo.gl/MtTiVnRzfeJ8AVxv7) to see the sign in action.

## Installation

Largely following [this guide](https://opensource.com/article/21/1/light-display-raspberry-pi).

This is on a fresh install of 64-bit Ubuntu Desktop 22.04.3 LTS for RPi.

1. `sudo apt install python3-dev`
2. Create a python virtual env, and activate it:
   - `mkdir ~/python_virtual_environments`
   - `python -m venv ~/python_virtual_environments/leds`
3. `pip install RPi.GPIO adafruit-circuitpython-neopixel Adafruit-Blinka`
4. To access the LEDs, you need to run python as root: 
   - `source ~/python_virtual_enviroments/leds/bin/activate`
   - `sudo /home/max/python_virtual_environments/leds/bin/python /home/max/dev/leds/LEDs.py`
