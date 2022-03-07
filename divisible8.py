def num(a):
    if (a % 8 == 0):
        return("It is divisible by 8")
    else:
        return("it is not disible by 8")
x = int(input("enter the number: "))
result = num(x)
print(result)
