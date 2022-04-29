import random

print('Дурна гра вгадай число (від 0 до 100)')
random.seed(55)
secret_num = random.randint(0, 100)
guess = None
while guess != secret_num:
    guess = int(input('Давай, вгадуй: '))

    if guess < secret_num:
        print('Ні, твоє число менше за загадане')
    elif guess > secret_num:
        print('Ні, твоє число більше за загадане')
print('Ти вгадав!!! Але призів не буде)))')

