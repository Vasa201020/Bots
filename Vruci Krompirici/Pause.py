import time
import random
import mouse

while True:
    wait = random.randint(3, 14)

    time.sleep(int(wait))

    mouse.move(1143, 387, absolute=True, duration=0.3)

    mouse.click('left')

    time.sleep(2)

    mouse.click('left')

    print("click" )
