fruits = ['🍊', '🍏', '🍊', '🍌', '🍉', '🍉', '🍌', '🍌', '🍋', '🍑']
print(fruits)

fruits = {'🍊', '🍏', '🍊', '🍌', '🍉', '🍉', '🍌', '🍌', '🍋', '🍑'}
print(fruits)

something = (1, 2, 3)
test_set = {something, 23, 'cucumber'}
print(test_set)

fruits = ['🍊', '🍏', '🍊', '🍌', '🍉', '🍉', '🍌', '🍌', '🍋', '🍑']
print(set(fruits))

fruits = ['🍊', '🍏', '🍊', '🍌', '🍉', '🍉', '🍌', '🍌', '🍋', '🍑']
fruits = set(fruits)
print(fruits)
fruits.discard('🍏')
print(fruits)
fruits.remove('🍑')
print(fruits)

# fruits.remove('🥒') # видасть помилку якщо його немає в списку
# fruits.discard('🥒')

fruits.add('🍐')
fruits.add('🍌')
print(fruits)
fruits.update(['🍐','🥝', '🍒'])
print(fruits)

fruits.clear()
print(fruits)


fruits = {'🍏', '🍑', '🍋', '🍊', '🍉', '🍌', '🥒'}
vegetables = {'🥒', '🍅', '🍆', '🥦', '🥔', '🍌'}

everything = fruits | vegetables  # Об'єднання (union)
everything = fruits.union(vegetables)
print(everything)

print(vegetables & fruits)  # Перетин (intersection)
print(vegetables.intersection(fruits))

print(vegetables - fruits)  # Різниця (difference)
print(vegetables.difference(fruits))
print(fruits - vegetables)  # Несиметрична операція

print(vegetables ^ fruits)  # Симетрична різниця (Symmetric Difference)

# Основні корисності типу set: унікальність елементів, операції з множинами (обʼєднання, перетин, різниця)

# Так само можно використовувати в циклах for
for fruit in fruits:
    print(fruit)
