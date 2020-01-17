# a tuple CAN'T be changed after it is created!!!

pi_tuple = (3, 1, 4, 1, 5, 9)
print(pi_tuple)

#transformam un tuple in lista
new_list = list(pi_tuple)
print(new_list)

#transformam o lista in tuple
new_tuple = tuple(new_list)
print(new_tuple)

print("Lenght of this tuple is:", len(new_tuple))
print("The minimum value of this tuple is: ", min(new_tuple))
print("The maximum value of this tuple is: ", max(new_tuple))