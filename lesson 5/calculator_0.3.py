print('Ласкаво просимо до неймовірного калькулятора (версія 0.3)')
sym = input('Оберіть операцію (+, -, *, /, +++): ')
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
        try:
            (num, '/', num2, '=', num / num2)
        except ZeroDivisionError:
            print('∞')
            quit()
        print(num, '/', num2, '=', num / num2)
elif sym == '+++':
    num3 = None
    numbers = []
    while num3 != ' ':
        num3 = input('Введіть число: ')
        numbers.append(num3)
    for number in range(len(numbers[:-1])):
        numbers[number] = int(numbers[number])
    print(sum(numbers[:-1]))
else:
    print('Помилка!')
    
