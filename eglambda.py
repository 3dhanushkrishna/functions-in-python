a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))

sum = lambda x, y, z: x+y+z
result = sum(a,b,c)
print(result)