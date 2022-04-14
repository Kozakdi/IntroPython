hanry_is_duck = True
quacker_is_duck = True
me_is_duck = False

print(hanry_is_duck and quacker_is_duck)
print(hanry_is_duck and me_is_duck)

print(hanry_is_duck or me_is_duck)
friend_is_duck = False
print(me_is_duck or friend_is_duck)

print(not me_is_duck)
print(hanry_is_duck and not me_is_duck)


print(True and True) # True
print(True and False) # False
print(True or False) # True
print(False or False) # False
print(not False) # True
print(not True) #False

# можна поєднувати
print(True and not False) # True
print(True and True and True and False) #False
print(True or False and True) #True

# скобками можна групувати
print(True or False and False) #true
print((True or False) and False) #false


number = 5 # input
print(number > 0 and number < 10)
print(0 < number < 10)


print(number == 5 or number == 10)

text = 'Cucumber'
print('r' in text and 'c' in text)
print('z' not in text)


