def fac(n):
    if n==0:
        return 1
    return n*fac(n-1)

result=fac(5)
print(result)