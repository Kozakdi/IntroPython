print('Вас вітає конвертер смайликів у емоджі 😈 🙂 😠 😂 🙁')
emoji = input('Введіть текст для конвертації: ')
print(
    emoji.replace('>:)', '😈')
    .replace('>:(', '😠')
    .replace('XD', '😂')
    .replace(':)', '🙂')
    .replace(':(', '🙁')
)
