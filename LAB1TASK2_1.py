def sphere_volume(r):
    d = 4 / 3
    r = int(r)
    v = d * 3.14 * r ** 3
    return v

r = input("Enter radious to find volume:")
print(sphere_volume(r))
