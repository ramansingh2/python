x=lambda a:a+5
print(x(5))


y=lambda a,b:a*b
print(y(6,7))


u=lambda a,b,c:a+b+c
print(u(4,5,6))



def myf(n):
    return lambda a:a*n

mydoubler=myf(2)
print(mydoubler(5))


def myfun(m):
    return lambda b:b+b+m
myadd=myfun(2)
print(myadd(5))