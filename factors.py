def factors(n):
    factor =[]
    i=1
    while i<=n:
        if n%i==0:
            factor.append(i)
        i+=1
    factor.append(n)
    return factor

def isprime(n):
    if n==1:
        return "neither prime nor composite"
    else:
        return (factors(n)==[1,n])
print(factors(20))
print(isprime(1))