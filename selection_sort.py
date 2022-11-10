def select(l):
    for i in range(len(l)):
        min=i
        for j in range(i,len(l)):
            if l[i]>l[j]:
                min=j
                l[i],l[j]=l[j],l[i]
    return l

l=[34,56,90,21,4,35,12,78]
print(select(l))