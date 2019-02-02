def ack(m,n):
    m = int(m)
    n = int(n)
    ans = 0
    if m == 0:
        ans = n + 1
    elif m > 0 and n == 0:
        ans = ack(m-1,1)
    elif m > 0 and n > 0:
        temp = ack(m,n - 1)
        ans = ack(m - 1,temp)
    else:
        return ans
    return ans

m = input("Enter value for m:")
n = input("Enter value for n:")
print(ack(m,n))
   
