some_list =['python', 'cora', 'tasks', 'cat', 'washing the car', 'food']

print('First item in list is ', some_list[0])

some_list[0] = "programming"
print('First item in list is ', some_list[0])

print(some_list[1:4])

another_list = ['go to the gym', 'meditate', 'drink water', 'eat healier', 'loose some weight']

to_do_list = [some_list, another_list]
print(to_do_list)

print(to_do_list[0][1])

some_list.append('cat food')
print(to_do_list)

another_list.insert(1, "yoga")
print(to_do_list)

another_list.remove("loose some weight")
print(to_do_list)

some_list.sort()
print(some_list)

another_list.reverse()
print(another_list)

del some_list[2]
print(some_list)

add_lists = some_list + another_list
print(add_lists)

print(len(to_do_list))
print(len(add_lists))

print(max(to_do_list))
print(max(add_lists))

print(min(to_do_list))
print(min(add_lists))


list_of_numbers = [i for i in range(0,10)]
print("Numerele sunt: ", list_of_numbers)

list_of_numbers_easy = list(range(10))
print("Varianta mai usoara :", list_of_numbers_easy)

list_of_even_numbers = list(range(0,10,2))  
#list_of_even_numbers = [i for i in range(0,10,2)]
print(list_of_even_numbers)

#create a list from comma separated string

string = "hi, hello, welcome, how, are you?"
string_list = string.split(',')
print("Lista cu virgule", string_list)

#string to list
string1 = "hello"
string2list = list(string1)
print("Un cuvant transformat in lista :", string2list)

#integers to list
integer = 123456789
integer2list = [int(i) for i in str(integer)]
print("un numar transformat in lista: ", integer2list)

#dictionary keys/values to list
my_dictionary = {1:'a', 2:'b', 3:'c', 4:'d'}
print("Dictionar :", my_dictionary)

key_list = list(my_dictionary.keys())
print("keys of dictionary", key_list)

value_list = list(my_dictionary.values())
print("Values of dictionary", value_list)

#built in functions for list in python

list1 = ['cat', 2, 55, 'dogs', "food", 3.14]
print("Lista initiala", list1)

#adaugam un element la finalul listei
list1.append('goat')
print("Lista modificata", list1)

#extindem o lista cu o alta lista

list2 = ['apples','pears', 'peas', 789, 0.1]
list1.extend(list2)
print("Lista extinsa ", list1)

#adaugarea unui element nou intr-o lista la o locatie particulara
list1.insert(2, 'owl')
print("Lista cu noul element", list1)

#aflarea indexului unui element din lista
food_index = list1.index('food')
print('Acesta este indexul pentru food: ', food_index)

list1.insert(food_index+1, 'duck')
print('Noua lista: ', list1)

#eliminam un element din lista
list1.remove(2)
print('Noua lista: ', list1)

#eliminam si returnam un element
popped = list1.pop()  #elimina ultimul element
print('elementul eliminat este:', popped)
popped1 = list1.pop(1)
print('elementul eliminat este: ', popped1)
print('Noua lista', list1)

#sortam elementele in ordine crescatoare 
lista = [1, 3, 56, 98, -2, 657, -86]
print('Lista initiala este: ', lista)
lista.sort()
print('Lista sortata este: ', lista)
lista.sort(reverse=True)
print('Lista sortata invers este: ', lista)

