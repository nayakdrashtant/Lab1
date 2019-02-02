def is_triangle(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)
    if a == b == c:
        return True
    else:
        return False

a = input("Enter value for stick1:")
b = input("Enter value for stick2:")
c = input("Enter value for stick3:")
print("Is Trianlge:", is_triangle(a,b,c))
