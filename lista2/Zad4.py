def multiply(m,n,acc=0):
    if m == 0 or n == 0:
        return acc
    elif m == 1:
        return n + acc
    elif n == 1:
        return m + acc
    else:
        if m <= n:
            return multiply(m-1,n,n+acc)
        elif m > n:
            return multiply(m,n-1,m+acc)

print(multiply(1,12))



