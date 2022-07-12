#1
print('Добро пожаловать в НеВеРоЯтНыЙ калькулятор (версия 0.1)')
print('Сейчас мы сложим 2 любых целых числа 💪')
a = input('Введите первое число: ')
b = input('Введите второе число: ')

print(a, '+', b, '=', int(a) + int(b))

#2
level = input('Оцените свой уровень стресса положительным целым числом: ')
level = int(level)
print('A' * level + '!')

#3
print('Добро пожаловать в НеВеРоЯтНыЙ калькулятор (версия 0.2)')
print('Теперь я умею складывать, отнимать, умножать и делить 2 любых целых числа 💪')
operation = input('Выберите операцию (+, -, *, /): ')
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

result = None
if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    result = a / b
else:
    print('Неизвестная операция', operation, 'выберите одно из: +, -, *, /')
    exit(1)

print(a, operation, b, '=', result)



#4
print('Я молодший брат НеЙмОвІрНоГо калькулятора - ймовірний порівняч 👋')
print('Потрібна допомога із числами? Введи два цілих числа і я підкажу яке більше, а яке менше')

first = int(input('Давай перше: '))
second = int(input('Давай друге: '))

if first < second:
    print('Перше менше другого!', first, '<', second)
elif first > second:
    print('Перше більше другого!', first, '>', second)
else:
    print('ОГО! А числа то, однакові!', first, '=', second)

#5
# Square
# SIZE = 10
# for x in range(SIZE):
#     for y in range(SIZE):
#         place(x, 0, y)

# Cube
# SIZE = 5
# for x in range(SIZE):
#     for y in range(SIZE):
#         for z in range(SIZE):
#             if sum((x in (0, (SIZE - 1)), y in (0, (SIZE - 1)), z in (0, (SIZE - 1)),)) >= 2:
#                 place(x, y, z)

# Circle
# RADIUS = 10
# RAD2 = RADIUS ** 2
# for x in range(-RADIUS, RADIUS + 1):
#     for y in range(-RADIUS, RADIUS + 1):
#         if RAD2 * 0.9 <= x ** 2 + y ** 2 <= RAD2 * 1.1:
#             place(x, y, 0)


#6

print('Щас найдем огурец 🥒')
text = input('Введите фразу со словом "cucumber": ')

cucumber_i = text.find('cucumber')
if cucumber_i >= 0:
    print(text[cucumber_i:])
else:
    print('"cucumber" не найден... Ну блин, я ж просил 😢')


#7
print('Вас приветствует конвертер смайликов в емоджи 🙂😂🙁😠😈')
text = input('Введите текст для конвертации: ')

print(
    text.replace('>:)', '😈')
    .replace('>:(', '😠')
    .replace(':(', '🙁')
    .replace('XD', '😂')
    .replace(':)', '🙂')
)


#8

print('Ласкаво просимо до ЧуДоВоГо калькулятору (версія 0.3)')
print('Тепер я також вмію швидко складати багато чисел. Спробуй нову операцію "+++" 😉')
operation = input('Оберіть операцію (+, -, *, /, +++): ')

if operation in ('+', '-', '*', '/'):
    a = int(input('Введіть перше число: '))
    b = int(input('Введіть друге число: '))
elif operation in ('+++',):
    print('Введіть декілька чисел, по заверщенню залиште строку пустою')
    nums = []
    input_str = True

    while input_str:
        input_str = input(
            'Введіть число та натисніть Enter (якщо бажаете завершити, просто натисніть Enter):'
        )
        if input_str:
            nums.append(int(input_str))

result = None
if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    result = a / b
elif operation == '+++':
    result = sum(nums)
else:
    print('Невідома операція', operation, 'оберіть одне з: +, -, *, /, +++')

if result is not None:
    print('Результат:', result)


#9
import time
import random


print('Зараз буде змійка :3')
time.sleep(1)

width = 20
position = width // 2

while True:
    try:
        time.sleep(0.1)
        position += random.choice([-1, 0, 1])
        position = min(max(0, position), width - 1)

        row = ' ' * (position - 1) + '*' + ' ' * (width - position)
        print(row)
    except KeyboardInterrupt:
        row = ' ' * (position - 4) + '0_0' + ' ' * (width - position)
        print(row)
        break

#10

BASE = 24
CHAR_BASE = ord('A') - 1

print(f'Ласкаво просимо у конвертер системи числення з базою {BASE} в десяткову.')
print('Допустимі символи та їх значення:')
for i in range(BASE):
    if i < 10:
        print(f'{i} = {i}')
    else:
        print(f'{chr(CHAR_BASE + i - 9)} = {i}')

print()
inp_num = input(f'Введіть число в базі {BASE}: ').upper()

dec_value = 0
for i, char in enumerate(reversed(inp_num)):
    if char.isdigit():
        dec_value += int(char) * BASE ** i
    elif 9 < ord(char) - CHAR_BASE + 9 < BASE:
        dec_value += (ord(char) - CHAR_BASE + 9) * BASE ** i
    else:
        print('Введене число не відповідає базі.')
        dec_value = None
        break

if dec_value is not None:
    print(f'Ваше число в десятковій системі числення: {dec_value}')


#11
print('Ласкаво просимо в шифрувальник/дешифрувальник для шифру Цезаря.')

action = input('Введіть "1" для шифрування, "2" для дешифрування: ').lower()
assert action in ('1', '2'), 'Невідома дія'

text = input('Введіть текст (тільки літери [a-z, A-Z]): ')
key = int(input('Введіть ключ: '))

result = ''

if action == '2':
    key = -key

for char in text:
    if ord('a') <= ord(char) <= ord('z'):
        char_shift = ord('a')
    elif ord('A') <= ord(char) <= ord('Z'):
        char_shift = ord('A')
    else:
        result += char
        continue

    result += chr(char_shift + (ord(char) - char_shift + key) % 26)

if result:
    print(f'Результат: {result}')


#12
print('Привіт! Я тут щоб жувати жувачку та рахувати кількість символів у тексті 😎')
print('Як бачищ, жувати жувачку я не можу...')
text = input('Тож давай текст: ')

chars_count = {}
for char in text:
    chars_count[char] = chars_count.get(char, 0) + 1

for char, count in chars_count.items():
    print(f'- Символ "{char}" зустрічається {count} разів')



#13

def input_num(message='Введіть число: ', allow_empty=False):
    while True:
        inp_ = input(message)

        if inp_ == '' and allow_empty:
            return inp_

        try:
            return float(inp_)
        except ValueError:
            print('Це не число. Спробуйте ще раз.')


print('Ласкаво просимо до ЧуДоВоГо калькулятору (версія 0.4)')
print('Тепер я вмію працювати з будь-якими числами, а також перевіряю введені дані.')
operation = input('Оберіть операцію (+, -, *, /, +++): ')

if operation in ('+', '-', '*', '/'):
    a = input_num('Введіть перше число: ')
    b = input_num('Введіть друге число: ')
elif operation in ('+++',):
    print('Введіть декілька чисел, по завершенню залиште строку пустою')
    nums = []
    input_str = True

    while input_str:
        input_str = input_num(
            'Введіть число та натисніть Enter (якщо бажаете завершити, просто натисніть Enter): ',
            allow_empty=True,
        )
        if input_str:
            nums.append(int(input_str))
else:
    print('Невідома операція', operation, 'оберіть одне з: +, -, *, /, +++')


result = None
if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    result = a / b
elif operation == '+++':
    result = sum(nums)

if result is not None:
    print('Результат:', result)


#14
import random

numbers = [random.randint(0, 100) for _ in range(10)]
print('Initial list:', numbers)


def sort_list(numbers):
    sorted_numbers = numbers[::]
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if sorted_numbers[i] > sorted_numbers[j]:
                sorted_numbers[i], sorted_numbers[j] = (
                    sorted_numbers[j],
                    sorted_numbers[i],
                )

    return sorted_numbers


print('Sorted list:', sort_list(numbers))


#15
import argparse
from pathlib import Path
import random

import requests

URL = 'http://placekitten.com'
SIZE_RANGE = (100, 1000)


def get_cat_picture(width, height, filename, gray=False):
    url = f'{URL}{"/g" if gray else ""}/{width}/{height}'
    response = requests.get(url)

    with open(filename, 'wb') as catfile:
        for chunk in response:
            catfile.write(chunk)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Створювач кицьок :3')
    parser.add_argument('amount', type=int, help='Кількість картинок з кицями')
    parser.add_argument(
        'out_dir', nargs='?', default='.', help='Директорія для збереження картинок',
    )
    parser.add_argument(
        '--gray',
        action='store_true',
        default=False,
        help='Створювати чорно-білих кицьок',
    )

    args = parser.parse_args()

    print('Вітаю у створювачі кицьок :3')
    print(
        f'Зараз створю тобі {args.amount} картинок '
        f'з {"чорно-білими " if args.gray else ""}'
        f'кицями у директорії {args.out_dir}'
    )
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    for i in range(1, args.amount + 1):
        width = random.randint(*SIZE_RANGE)
        height = random.randint(*SIZE_RANGE)
        filename = out_dir / f'cat_{i}.jpg'

        print(f'Створюю котика номер {i} у розмірі {width}x{height}')
        get_cat_picture(width, height, filename, gray=args.gray)

    print('Створення кицьок завершено! Насолоджуйтеся :3')



#16

import csv
import json
from pathlib import Path

DATA_FILE = Path('people_db.json')
RESULT_FILE = Path('invite.csv')


def rules(person):
    return all(
        (
            not person['company_name'],
            person['phone'],
            'software' in person['job_title'].lower(),
        )
    )


with open(DATA_FILE) as people_file:
    people = json.load(people_file)


with open(RESULT_FILE, 'w') as result_file:
    csv_writer = csv.DictWriter(result_file, fieldnames=people[0].keys())
    csv_writer.writeheader()
    for person in filter(rules, people):
        csv_writer.writerow(person)


#17

print(
    'Привіт! Мені дуже потрібен Cucumber прямо зараз, введи мені Cucumber будь ласка!\n'
    'Але будь уважним, неймовірно важливо щоб Cucumber був гарний та без помилок!'
)


def validations(cucumber):
    assert (
        ' ' not in cucumber
    ), 'Щось я не памʼятаю щоб у Cucumber були пробіли. Буду вважати що це випадковість...'

    assert 'cucumber' in cucumber.lower(), 'Тут взагалі нема Cucumber!'

    assert cucumber.startswith('C'), (
        'О ні! Ну хто ж так робить!'
        ' Твій Cucumber починається з маленької літери, виправляй швиденько'
    )

    assert cucumber[1:].islower(), 'Що за кривий Cucumber? А ну вирівнюй!'

    assert cucumber.lower() == 'cucumber', 'Тут щось зайве - прибери'


while True:
    cucumber_input = input('Давай, я в тебе вірю: ')

    try:
        validations(cucumber_input)
    except AssertionError as error:
        print(error, '😡')
    else:
        print('Відмінно! Дуже дякую! Ти, буквально, врятував всесвіт 😊')
        break


#18
from abc import ABC, abstractmethod


class Input:
    """
    Base class to handle user input and validation.
    In the base - no validations are implemented.
    """

    _ERROR = 'Помилка введення'

    def __init__(self, message='Будь ласка, введіть текст'):
        self.message = message

    def ask(self):
        return self._valid_input()

    def _valid_input(self):
        message = self.message + (': ' if not self.message.endswith(': ') else ' ')
        while True:
            inp = input(message)
            try:
                return self._validate(inp)
            except (ValueError, AssertionError):
                print(self._get_error())

    def _validate(self, inp):
        return inp

    def _get_error(self):
        return self._ERROR


class NumInput(Input):
    """Handle user input and validate it's a number"""

    _ERROR = 'Очікувалося число :/'

    def __init__(self, message='Будь ласка, введіть число'):
        super().__init__(message)

    def _validate(self, inp):
        return float(inp)


class MultiNumInput(NumInput):
    """
    Handle user input and validate it's a number.
    Repeat specified amount of time (if amount = '*' - until user input is empty).
    """

    def __init__(self, message='Будь ласка, введіть число', amount='*'):
        super().__init__(message)
        self._amount = amount

    def ask(self):
        inputs = []
        next_message = self.message + ' (введіть пустий рядок, щоб закінчити)'
        while self._amount == '*' or len(inputs) < self._amount:
            inp = self._valid_input()
            if inp is None:
                break
            inputs.append(inp)

            if self._amount == '*':
                self.message = next_message

        return inputs

    def _validate(self, inp):
        if self._amount == '*' and inp == '':
            return None

        return super()._validate(inp)


class Operation(ABC):
    """Abstract base class for executing operations"""

    INPUT_HANDLER = None
    SYMBOL = None

    def __init__(self):
        assert self.SYMBOL is not None

        self._operands = self._input()

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    def _input(self):
        assert self.INPUT_HANDLER is not None
        return self.INPUT_HANDLER.ask()

    @property
    @abstractmethod
    def result(self):
        raise NotImplementedError


class BinaryOperation(Operation, ABC):
    """Abstract base for binary operations (with two operands)"""

    INPUT_HANDLER = MultiNumInput(amount=2)

    def __init__(self):
        super().__init__()

        self._a, self._b = self._operands

    def __str__(self):
        return f'{self._a} {self.SYMBOL} {self._b}'


class Add(BinaryOperation):
    SYMBOL = '+'

    @property
    def result(self):
        return self._a + self._b


class Substract(BinaryOperation):
    SYMBOL = '-'

    @property
    def result(self):
        return self._a - self._b


class Multiply(BinaryOperation):
    SYMBOL = '*'

    @property
    def result(self):
        return self._a * self._b


class Divide(BinaryOperation):
    SYMBOL = '/'

    @property
    def result(self):
        try:
            return self._a / self._b
        except ZeroDivisionError:
            return '∞'


class MultiSum(Operation):
    """Sum any amount of numbers"""

    INPUT_HANDLER = MultiNumInput()
    SYMBOL = '+++'

    def __str__(self):
        return ' + '.join(map(str, self._operands))

    @property
    def result(self):
        return sum(self._operands)


OPERATIONS = (
    Add,
    Substract,
    Multiply,
    Divide,
    MultiSum,
)


class OperationSelect(Input):
    """Handle user input and validate it's valid operation"""

    def __init__(self):
        super().__init__(f'Будь ласка, оберіть операцію {list(self._operations_symbols)}')

    @property
    def _operations_symbols(self):
        return (operation.SYMBOL for operation in OPERATIONS)

    def _validate(self, inp):
        assert inp in self._operations_symbols
        return inp

    def _get_error(self):
        operations = ', '.join(self._operations_symbols)
        return f'Невідома операція. Можливі операції: {operations}'


class Calculator:
    """Main calculator logic"""

    WELCOME_MESSAGE = (
        'Ласкаво просимо до ЧуДоВоГо калькулятору (версія 0.5).\n'
        'Для тебе нічого не змінилося. Але я тепер серйозний 😎'
    )

    def execute(self):
        print(self.WELCOME_MESSAGE)

        operation = self._find_operation(OperationSelect().ask())
        operation = operation()

        print(f'{operation} = {operation.result}')

    def _find_operation(self, symbol):
        for operation in OPERATIONS:
            if operation.SYMBOL == symbol:
                return operation

        raise ValueError(f'Unknown operation {symbol}')


if __name__ == '__main__':
    calculator = Calculator()
    calculator.execute()


#19
from typing import Tuple
from concurrent.futures import ThreadPoolExecutor

import requests

URL = 'http://code.qqmber.wtf/guess/'


def guess_password(password: str) -> Tuple[bool, str, requests.Response]:
    print(password)
    response = requests.post(URL, json={'password': password})
    return response.status_code == 200, password, response


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=32) as executor:
        for success, password, response in executor.map(guess_password, (str(i).zfill(3) for i in range(1000))):
            print(f'Check: {password}, {response}')
            if success:
                print(f'Done, password is {password}')
                break


#20
import math
import random
from typing import Generator, Optional


class Board:
    def __init__(self, size: int = 3):
        self._size = size
        self._board = [[' ' for _ in range(self._size)] for _ in range(self._size)]

    def __str__(self):
        """
        Render board to string like that:
          1 2 3
         ┏━┳━┳━┓
        A┃O┃X┃O┃
         ┣━╋━╋━┫
        B┃X┃O┃X┃
         ┣━╋━╋━┫
        C┃O┃X┃O┃
         ┗━┻━┻━┛
        """
        board_str = '  ' + ' '.join(map(str, range(1, self._size + 1))) + '\n'  # numbers row
        board_str += ' ┏' + '┳'.join('━' for _ in range(self._size)) + '┓\n'  # top border

        for i in range(self._size):
            board_str += f'{chr(i + ord("A"))}┃' + '┃'.join(self._board[i]) + '┃\n'
            if i < self._size - 1:
                board_str += ' ┣' + '╋'.join('━' for _ in range(self._size)) + '┫\n'
            else:
                board_str += ' ┗' + '┻'.join('━' for _ in range(self._size)) + '┛\n'  # bottom border

        return board_str

    def __getitem__(self, coordinates: str) -> str:
        y, x = self.coords_to_index(coordinates)
        return self._board[y][x]

    def __setitem__(self, coordinates: str, value: str):
        y, x = self.coords_to_index(coordinates)
        self._board[y][x] = value

    def __iter__(self) -> Generator[tuple[str, ...], None, None]:
        for row in self._board:
            yield tuple(row)

    @property
    def size(self) -> int:
        return self._size

    def find_all(self, value: str) -> Generator[str, None, None]:
        for y, row in enumerate(self._board):
            for x, cell in enumerate(row):
                if cell == value:
                    yield self.index_to_coords(y, x)

    def copy(self) -> 'Board':
        copy_board = self.__class__(self._size)
        copy_board._board = [list(row) for row in self]

        return copy_board

    @staticmethod
    def coords_to_index(coordinates: str) -> tuple[int, int]:
        assert len(coordinates) == 2, f'Invalid coordinates: {coordinates}'

        coordinates = coordinates.upper()

        x = None
        y = None

        for char in coordinates:
            if char.isdigit():
                x = int(char) - 1
            elif char.isalpha():
                y = ord(char) - ord('A')
            else:
                raise AssertionError(f'Invalid coordinates: {coordinates}')

        assert x is not None and y is not None, f'Invalid coordinates: {coordinates}'

        return y, x

    @staticmethod
    def index_to_coords(y: int, x: int) -> str:
        return f'{chr(y + ord("A"))}{x + 1}'


class XOXOGame:
    def __init__(self):
        self._board = Board()

    def __str__(self):
        str_ = 'XOXO'.center(4 + self._board.size * 2, '=') + '\n\n'  # title
        return str_ + str(self._board)

    @property
    def board(self) -> Board:
        return self._board

    def reset(self):
        self._board = Board()

    def make_move(self, move: str, player: str):
        try:
            assert self._board[move] == ' ', 'Invalid move, square is not empty'
            self._board[move] = player
        except IndexError:
            raise AssertionError(f'Invalid move, out of board')

    def check_win(self) -> Optional[str]:
        for player in ('X', 'O'):
            ys = []
            xs = []
            for coords in self._board.find_all(player):
                y, x = Board.coords_to_index(coords)
                ys.append(y)
                xs.append(x)

            for row in self._board:
                if row.count(player) == self._board.size:
                    return player

            for column in range(self._board.size):
                if [row[column] for row in self._board].count(player) == self._board.size:
                    return player

            if sum(x == y for x, y in zip(xs, ys)) == self._board.size:  # diagonal row from A1 to C3
                return player
            elif sum((2 - x) == y for x, y in zip(xs, ys)) == self._board.size:  # diagonal row from C3 to A1
                return player

        return None

    def copy(self):
        copy_game = self.__class__()
        copy_game._board = self._board.copy()

        return copy_game


class PlayerInterface:
    VALUE = 'X'

    def __init__(self, game: XOXOGame):
        self._game = game

    def make_move(self):
        while True:
            move = input('Enter your move: ')
            try:
                self._game.make_move(move, self.VALUE)
                break
            except AssertionError as e:
                print(e)


class ComputerInterface:
    VALUE = 'O'

    def __init__(self, game: XOXOGame):
        self._game = game

    def _minimax_move(self, game: XOXOGame, player: str) -> tuple[str, float]:
        """Minimax algorithm to find the best move"""
        best = ('', -math.inf if player == self.VALUE else math.inf)

        winner = game.check_win()
        if winner is not None:
            return ('', 1 if winner == self.VALUE else -1)

        possible_moves = list(game.board.find_all(' '))
        if len(possible_moves) == 0:
            return ('', 0)

        for move in possible_moves:
            copy_game = game.copy()
            copy_game.make_move(move, player)
            _, score = self._minimax_move(copy_game, 'O' if player == 'X' else 'X')

            if player == self.VALUE:
                if score > best[1]:
                    best = (move, score)
            else:
                if score < best[1]:
                    best = (move, score)

        return best

    def make_move(self):
        # if it's a first move in a game - don't think, just play randomly
        legit_moves = list(self._game.board.find_all(' '))
        if len(legit_moves) == self._game.board.size ** 2:
            move = random.choice(legit_moves)
        else:
            move, _ = self._minimax_move(self._game, self.VALUE)

        print(f'Computer move: {move}')
        self._game.make_move(move, self.VALUE)


if __name__ == '__main__':
    game = XOXOGame()
    player = PlayerInterface(game)
    computer = ComputerInterface(game)

    current = player if random.randint(0, 1) == 0 else computer

    while True:
        print(game)

        winner = game.check_win()
        if winner:
            print(f'{winner} wins!')
            break

        if len(list(game.board.find_all(' '))) == 0:
            print('Tie!')
            break

        current.make_move()
        print()

        current = computer if current == player else player
