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


print("The following doors are open: ", end="")
print(*howmanydoors(0, 100))