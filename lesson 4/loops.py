alphabet = 'abcdefghijklmnopqrstuvwxyz'
for letter in alphabet:
    print(letter)
    print(letter.capitalize())


digits = '12348457395619365021'
for digit in digits:
    if int(digit) < 5:
        print(digit)

counter = 0
while counter <= 100:
    print(counter)
    counter += 1

text = None
while text != '3':
    text = input('Введіть 3: ')
print('Дяк :3')

for num in range(10):
    print(num)

for num in range(10, 20):
    print(num)

for num in range(10, 20, 2):
    print(num)

for num in range(100, 10, -1):
    print(num)  
    