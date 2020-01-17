import math

numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
print("The list of numbers is: ", numbers)
minimum = numbers[0]
maximum = numbers[0]

for i in range(len(numbers)):
    if numbers[i] < minimum:
        minimum = numbers[i]
    if numbers[i] > maximum:
        maximum = numbers[i]

print("Minimimum of the elements in numbers is: ", minimum)
print("Maximum of the elements in numbers is: ", maximum)

suma = 0
for i in range(len(numbers)):
    suma += numbers[i]

print("The sum of the elements of numbers is:", suma)
avg = float(suma/len(numbers))
print("The average of the elements in numbers is: ", suma, "/", len(numbers), "=", avg)