def check_fermat(a,b,c,n):
    a = int(a)
    b = int(b)
    c = int(c)
    n = int(n)
    ab = (a ** n + b ** n)
    c = (c ** n)
    if ab == c:
        print("Holy smokes, Fermat was wron")
    else:
        print("No, that doesn’t work")

a = input("a:")
b = input("b:")
c = input("c:")
n = input("n:")
check_fermat(a,b,c,n)
