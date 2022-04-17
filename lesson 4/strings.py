text = 'Cucumber'
print(text.lower())
print(text.upper())

text = 'CuCuMber'
print(text.capitalize())
print(text.swapcase())


text = 'CuCumbers are Cool'
print(text.capitalize())

text = '   a  '
print(bool(text))
print(text.isspace())

text = 'abcbd'
print(text.isalpha())
text = '123'
print(text.isnumeric())

text = 'Cucumber or not?'
print(text.startswith('Cucumber'))
print(text.endswith('?'))

text = 'cucumber cucumber banana cucumber'
print(text.count('cucumber'))
print(text.count('u'))
print(text.replace('banana', 'cucumber'))
print(text.replace('a', 'u'))
print(text.replace('a', ' '))
print(text.replace('banana', 'cucumber').count('cucumber'))


text = 'abcdef'
#       012345
print(text[0])

print(text['1'])  # індексами не можуть бути строки

print(text[-1]) # завжди поверне останній елемент строки

print(text.index('d'))
print(text[text.index('d')])
print(text.index('bcd'))
print(text.find('z'))
print(text.find('d'))

template = 'I like {} and {}'
liked = 'cucumber'
other_liked = 'bananas'
print(template.format(liked, other_liked))

template = 'I like {} - so I will go and buy {}'
print(template.format(liked, liked))

template = 'I like {obj} - so I will go and buy {obj}'
print(template.format(obj=liked))

template = 'I like {1} - so I will go and buy {0}'
print(template.format(liked, other_liked))

print(f'I like {liked}')
print(f'I like {liked * 10}')


text = 'I don\'t like banana'
#       0 123 45 6789....
print(text)
print(text[6])
print(text[6:])
print(text[8:10])
print(text[2:10:2])
print(text[2::2])

text = '0123456789'
print(text[1::2])
 