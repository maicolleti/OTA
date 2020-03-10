from machine import Pin
from time import sleep


def led():

    led_b = Pin(2, Pin.OUT)
    while True:
        led_b.value(not led_b.value())
        sleep(0.5)
