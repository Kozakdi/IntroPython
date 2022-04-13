# Створюємо змінні
hanry = 'White Duck'
quacker = 'Black Duck'
print('Hanry is', hanry)
print('Quacker is', quacker)

# Змінюємо змінні місцями неправильно
hanry = quacker
quacker = hanry
print('Hanry is', hanry)
print('Quacker is', quacker)

# Змінюємо змінні місцями правильно, але нудно
box = hanry
hanry = quacker
quacker = box
print('Hanry is', hanry)
print('Quacker is', quacker)

# Змінюємо змінні місцями по пайтоновськи
hanry, quacker = quacker, hanry
print('Hanry is', hanry)
print('Quacker is', quacker)

# Так не можна називати змінні:
# 1_variable = 1
# Так можна:
# variable_1 = 1 

