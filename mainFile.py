# Open a file

f = open("main.txt", "r")

print("the name of this file is ", f.name)
print("The close status of this file is ", f.closed)
print("The mode of this file is ", f.mode)

string = f.read()
print(string)
