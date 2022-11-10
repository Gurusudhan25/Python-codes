#binary search for list

def bs(l,v):                    
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    length=len(l)
    if v==l[length//2]:
        return True
    if v<l[length//2]:
        for i in range(length//2+1):
            if l[i]==v:
                return True
    if v>l[length//2]:
        for i in range(length//2,length):
            if l[i]==v:
                return True
    return False

x=[2,3,4,5,1,23,320,40,350,450,70,431,5331,31,25]
print(bs(x,25))