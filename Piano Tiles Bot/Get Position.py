import mouse
from time import sleep

while True:
    pos = mouse.get_position()
    print(pos)
    sleep(1)
