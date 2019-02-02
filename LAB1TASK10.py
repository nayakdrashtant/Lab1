def is_between(x, y,z):
    if x <= y <= z:
        return True
    else:
        return False

x = input("Enter value for x:")
y = input("Enter value for y:")
z = input("Enter value for z:")
print(is_between(x,y,z))
