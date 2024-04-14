temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

print('extracting numbers from second week')
my_slice = temperatures[7:14]
print(my_slice)

print('extracting temperatures above 100')
my_slice = temperatures[23:30]
print(my_slice)

print('reversing list and extracting temperatures from 5th and 10th day')
temperatures.reverse()
print(temperatures)

my_slice = temperatures[5:11]
print(my_slice)
