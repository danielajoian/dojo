print("hello world")
# comments 
"""
multiline comment
"""
'''
multiline comment
'''

# Python variables
x = 34 # x is a integer
string = "This is me" # this a string variable
y = 3.4 # float variable
 
'''
  Rules for creating variables in python:
1. It must start with a letter or a underscore
2. It cannot start with a number
3. It can only contain alphanumeric caracters or a underscore
4. Are case sensitive

'''

print(type(x))
print("the sum of x+y is ", x+y)
 
'''
There are 4 types of collections in python:
1. lists []  - can change the values, is ordered
2. tuple ()  - can't change the values
3. set  {}     - a colection of values unordoned and unindexed; no duplicates
4. dictionary {key:val, key1:val1} - keys and values
'''

# List
l1 = [2, 343, 5, 34]
print("this is a list", l1)
print(l1[0])


# Tuple
t1 = (1, 4, 5)
print("my tuple is", t1)

# Set
set = {1, 2, 4, 5, 6, 1, 2, 5}
print(set)

# Dictionary
myD = {
    "harry" : "dog",
    "mac" : "cat",
    "pisi" : "duck"
 }
print(myD)
print(myD["pisi"])
print(myD.get("harry"))

# If else conditionals
a = 34
b = 3
c = 12
d = input("Enter the number \n") # d is a string
d = int(d)
print(type(d))
print(d)



if d>a:
    print("a=", a, "d is greater")

elif d==a:
    print("d is equal to a")

else:
    print(a, "d is not greater")

# Loops in python while and for
i = 0

while i<10:
    print("hello")
    i +=1


for i in range(0, 12):
    print(i)

# iterate a list
fruits = [25,"Apples", "Pears", "Melons", "Cherry"]
for item in fruits:
    print("fruit:", item)


# Functions - performs an action

def myfunction(list1):
    for item in list1:
        print("The value of item is: ", item)

myfunction(fruits)



