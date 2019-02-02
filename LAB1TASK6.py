def evenodd(num):
    num = int(num)
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

x = input("Enter num to check its even or not:")
print("Num is:",evenodd(x))
