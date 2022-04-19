empty = []
print(empty)

empty = list()
print(empty)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
print(numbers[0])
print(numbers[3])
print(numbers[4:8])
print(numbers[4:8:2])
print(numbers[::2])

stuff = [23, 2.5, 'cucumber', True, None, [1, 2, 3]]
print(stuff)
print(stuff[0] * stuff[1])
print(stuff[0] * stuff[2])

ducks = ['Hanry', 'Quacker']
new_ducks = ['Lupa', 'Pupa']
my_ducks = ducks + new_ducks + new_ducks
print(my_ducks)

my_ducks = ducks + new_ducks
print(my_ducks * 2)

print(my_ducks + ['Rose'])

my_ducks.append('Rose')
print(my_ducks)
print(len(my_ducks))
print(my_ducks.index('Lupa'))

my_ducks.append('Lupa')
print(my_ducks)
print(my_ducks.index('Lupa'))
print(my_ducks.count('Lupa'))

my_ducks.remove('Lupa')
print(my_ducks)

del my_ducks[-1]
print(my_ducks)
my_ducks.insert(0, 'Cucumber')
print(my_ducks)


my_ducks.append('Wilhelm')
print(my_ducks)

my_ducks.extend(['Wilhelm', 'Rose'])
print(my_ducks)

print(list('Cucumber'))


digits = [1, 2, 3, 6, 4, 3, 7, 8, 10]
for digit in digits:
    if digit < 5:
        print(digit)





