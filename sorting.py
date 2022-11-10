a=[]
n=int(input("Enter the array size:"))
for i in range(n):
    x=int(input("Enter array values:"))
    a.append(x)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]

print(a)