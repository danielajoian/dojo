
a = int(input(": "))
b = int(input(": "))
i = 0
def gcd(a, b):    
    if a!=0 and b!=0:
        return a/b
    elif a==0:
        return b
print(gcd(a, b))
  