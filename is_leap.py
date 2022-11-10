
def is_leap(n):
    leap=False
    if n%4==0:
        if n%100==0:
            if n%400==0:
                leap=True
        else:
            leap=True

        
    return leap


#print(is_leap(2100))
s=input("enter:")
s=s.split(" ")
l=[]
for x in s:
    x=x.capitalize()
    l.append(x)
l=" ".join(l)
print(l)

