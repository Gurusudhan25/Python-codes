'''def fib(n):
    fib_series=[]
    a,b=0,1
    fib_series.append(a)
    fib_series.append(b)
    for i in range(2,20):
        c=a+b
        if c>n:
            break
        fib_series.append(c)
        a=b
        b=c
    return fib_series[-1]
print(fib(100))

def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
            break
    else:
        return True
#print(prime(13))'''

import math 
import sorting

# def factorial(n):
#     return math.factorial(n)
# print(factorial(10))
