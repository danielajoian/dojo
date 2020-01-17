
def doors():
    i = 1
    while i <= 100:
        yield i
        i +=1

for i in doors():
    print("This doors are open: ", i)

def howmanydoors(x, y):
    opendoors = []
    for i in range(x, y+1):
        j = 1
        while j * j <= i:
            if j * j == i:
                opendoors.append(i)
            j += 1
        i += 1
    return opendoors

print('''
           ____________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|
''')
print("The following doors are open: ", end="")
print(*howmanydoors(0, 100))
  
