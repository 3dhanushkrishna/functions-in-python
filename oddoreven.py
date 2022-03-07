def checkoddoreven(a):
    if (a % 2 == 0):
        return "even"
    else:
        return "odd"
x = int(input("enter the number: "))
result = checkoddoreven(x)
print(result)
