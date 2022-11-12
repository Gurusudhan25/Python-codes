def bubblesort(arr):
    length = len(arr)
    while (length):
        for x in range(len(arr)-1):
            if arr[x]>arr[x+1]:
                arr[x],arr[x+1]=arr[x+1],arr[x]
                swap = True
        length -=1

    return arr
print(bubblesort([5,4,3,2,4,18,13,2,15,378]))
# the time complex of this sorting is O(n^2)