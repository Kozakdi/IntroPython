import random

print(random.random())  # [0, 1)

for _ in range(10):
    print(random.random())

random_nums = [random.random() for _ in range(10)]
print(random_nums)

print(random.randint(0, 100))
print(random.randrange(0, 100, 5))
print(random.uniform(0, 100))

fruits = ['🍊', '🍏', '🍌']
# fruit = fruits[random.randint(0, len(fruits) -1)]
fruit = random.choice(fruits)
print(fruit)

smoothie = random.choices(fruits, k=2)
print(smoothie)

fruits = ['🍊', '🍏', '🍌', '🍏']
print(fruits)
random.shuffle(fruits)
print(fruits)


random.seed(123)
print([random.randint(0, 10) for _ in range(10)])

random.seed(123)
print([random.randint(0, 10) for _ in range(10)])

random.seed(123)
print([random.randint(0, 10) for _ in range(100)])

