print('Ласкаво просимо до неймовірного калькулятора (версія 0.2)')
print('Тепер я вмію додавати, віднімати, ділити та множити 2 будь-яких цілих числа')
sym = input('Оберіть операцію (+, -, *, /): ')
if sym == '+' or sym == '-' or sym == '/' or sym == '*':
    num = int(input('Введіть перше число: '))
    num2 = int(input('Введіть друге число: '))
    if sym == '+':
        print(num, '+', num2, '=', num + num2)
    elif sym == '-':
        print(num, '-', num2, '=', num - num2)
    elif sym == '*':
        print(num, '*', num2, '=', num * num2)
    elif sym == '/':
        print(num, '/', num2, '=', num / num2)
else:
    print('Помилка!')
    