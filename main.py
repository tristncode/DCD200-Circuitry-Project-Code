import time
from adafruit_circuitplayground import cp

cp.detect_taps = 2

while True:
    if cp.button_a:
        cp.play_file("meow2.wav")
    if cp.button_b:
        cp.play_file("meow.wav")
    if cp.shake(shake_threshold=20):
        cp.play_file("meow3.wav")
    if cp.tapped:
        cp.play_file("purr.wav")
        time.sleep(0.1)