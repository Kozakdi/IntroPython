import time

print(time.time())
print(1970 + time.time() / 60 / 60 / 24 / 365)

start = time.time()
for i in range(10_000_000):
    i ** 2
end = time.time()

print(f'Time spent: {end - start}s')

start = time.time()
time.sleep(5)
end = time.time()

print(f'Time spent: {end - start}s')
