import time
import random
print('Зараз буде змійка')
snake = True
rndm = random.randint(0,10)
print(chr(32) * rndm + chr(42))
x = [rndm + 1, rndm - 1, rndm]
while snake:
    try:
        print(chr(32) * random.choice(x) + chr(42))
        start = time.time()
        time.sleep(0.1)
        end = time.time()
    except KeyboardInterrupt:
        print((chr(32) * random.choice(x) + ('0_0')))
        exit()


