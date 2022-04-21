fruits =('🍑', '🍌', '🍏')
my_fruit = fruits[1]

print(my_fruit)


fruits =('🍑')
try:
    my_fruit = fruits[1]
    print(my_fruit)
except:
    print('Oh no!')


fruits = ('🍑', )
try:
    my_fruit = fruits[1]
    print(my_fruit)
except IndexError:
    print('Oh no!')
finally:
    print('Yo!')
