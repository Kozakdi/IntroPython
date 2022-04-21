print(sum((1, 2, -3, 4,)))

scores = [25, 67, 76, 13, 34]
total = 0
for score in scores:
     total += score
print(total)
print(sum(scores))
print(sum(scores, 10))

word = 'cucumber'
if isinstance(word, str) and 'c' in word and word.startswith('cuc') and word.isalpha() and 'e' in word:
    print('success')


print(all((True, True, True, True))) # якщо буде хоч один елемент false, поверне false

if all((
        isinstance(word, str),
        'c' in word,
        word.startswith('cuc'),
        word.isalpha(),
        'e' in word,
    )):
    print('success')

# any = or
# all = and
