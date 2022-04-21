temperatures = [10, -10, 23, -5, 0, 13, -25, 14]
water_temperatures = []

for temperature in temperatures:
    if temperature > 0:
        water_temperatures.append(temperature)
print(water_temperatures)


#list comprehension
water_temperatures = [temp for temp in temperatures if temp > 0]
print(water_temperatures)

print([temp for temp in temperatures if temp > 0])

water_temperatures = [temp if temp > 0 else 1 for temp in temperatures]
print(water_temperatures)


destinations = ['49003', 'aaaaa', '', '49033', '490490', None, '49050', 'Urkposhta', '49005']
valid_destination = [dest for dest in destinations if dest and dest.isdigit() and len(dest) == 5]
print(valid_destination)

print(isinstance('abs', str)) 
print(isinstance(123, str)) 

destinations = ['49003', 'aaaaa', '', '49033', '490490', None, '49050', 'Urkposhta', '49005']
valid_destinations = []

for destination in destinations:
    if destination and destination.isdigit() and len(destination) == 5:
        valid_destinations.append(destination)
    else:
        valid_destinations.append('INVALID')

print(valid_destinations)

print([dest if dest and dest.isdigit() and len(dest) == 5 else 'INVALID' for dest in destinations])
