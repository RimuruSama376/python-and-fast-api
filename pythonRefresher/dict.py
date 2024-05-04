my_car = {
    'model': 'ford',
    'make': 'Explorer',
    'year': '2018',
    'mileage': 40000
}

print(my_car)

my_car2 = my_car.copy()

for x, y in my_car.items():
    print(x, y)

my_car2['numberOfTires'] = 4

my_car2.pop('mileage')

for x, y in my_car2.items():
    print(x)
print(my_car)
print(my_car2.items())
