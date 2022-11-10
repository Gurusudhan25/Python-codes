def valueequalsindex(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]==l[j]:
                del(l[j],j)
                print(l)
    result=[]
    for i in l:
        a=l.index(i)
        if i==a+1:
            result.append(i)
    return result
            
            

list=[11,2,6,6,7,5,5,2]
print(valueequalsindex(list))