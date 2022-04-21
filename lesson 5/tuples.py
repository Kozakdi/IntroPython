empty_tuple = ()
print(empty_tuple)
empty_tuple = tuple()
print(empty_tuple)

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(numbers[0])
print(numbers[3:5])

stuff = (23, 2.5, 'cucumber', True, False, [1, 2, 3], (1, 2, 3)) 
print(stuff)


ducks = ('Hanry', 'Quacker')
new_ducks = ('Lupa', 'Pupa')
my_ducks = ducks + new_ducks
print(my_ducks)
print(my_ducks * 2)

# Не працює метод append
my_ducks.append('Rose')
print(my_ducks)


print(my_ducks.index('Quacker'))
print(my_ducks[2])
print(my_ducks.count('Quacker'))

fruits = ('🍊', '🍏', '🍌', '🍉', '🍋', '🍑')
smoothie = fruits[0:1] + fruits[2:3] + fruits[5:6]
print(smoothie)

smoothie = list(fruits)
print(smoothie)

fruits = tuple(smoothie)
print(fruits)


print(range(10))
print(list(range(10)))
print(list(range(10, 100, 10)))


print('Опізнавач фруктів 3000')
fruits = ('🍊', '🍏', '🍌', '🍉', '🍋', '🍑')
item = input('Що розпізнати?')
if item in fruits:
    print(f'{item} це фрукт')
else:
     print(f'{item} це не фрукт')
