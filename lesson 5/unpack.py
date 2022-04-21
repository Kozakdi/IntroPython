fruits =('🍑', '🍌', '🍏')
peach, banana, apple = fruits
print(peach)
print(apple)
print(banana)


fruits =('🍑', '🍌', '🍏', '🥝')
peach, banana, apple, _ = fruits
print(peach)
print(apple)
print(banana)

fruits =('🍑', '🍌', '🍏', '🥝', '🍍')
peach, banana, apple, *_ = fruits
print(peach)
print(apple)
print(banana)


fruits =('🍑', '🍌', '🍏', '🥝', '🍍')
peach, banana, apple, *other_fruits = fruits
print(peach)
print(apple)
print(banana)
print(other_fruits)
