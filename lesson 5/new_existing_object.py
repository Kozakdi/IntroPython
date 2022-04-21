fruits = ['🍊', '🍏', '🍌', '🍉', '🍋', '🍑' ]
smoothie = fruits.copy()
smoothie.remove('🍏')
smoothie.remove('🍉')
smoothie.remove('🍋')

print(smoothie)
print(fruits)

print(smoothie is fruits)
print(smoothie == fruits)

a =[1, 2, 3]
b =[1, 2, 3]

print(a is b)
print(a == b)

fruits = ['🍊', '🍏', '🍌', '🍉', '🍋', '🍑' ]
print(fruits[2:5])
smoothie = fruits[::]
smoothie.remove('🍏')
smoothie.remove('🍉')
smoothie.remove('🍋')

print(smoothie)
print(fruits)



fruits = ['🍊', '🍏', '🍌', '🍉', '🍋', '🍑' ]
print(fruits + fruits)
print(fruits * 10)
print([0] * 100)
print(['🍏'] * 10)

smoothie = fruits
fruits.append('🍑')
fruits = fruits + ['🍊']
print(fruits)

print(smoothie)
print(fruits is smoothie)
