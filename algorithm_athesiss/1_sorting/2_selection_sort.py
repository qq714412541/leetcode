def selection_sort(arr:list):
    if len(arr) < 2:
        return arr
    else:
        for i in range(len(arr)):
            comp = float('inf')
            index = int
            temp = int
            for j in range(i,len(arr)):
                if comp > arr[j]:
                    comp = arr[j]
                    index = j
            temp = arr[i]
            arr[i] = comp
            arr[index] = temp
        return arr
    return arr

x = selection_sort([2,1,3,1,4,6,7,4,1,4,9,1])
print(x)

#1 comparabile number comp is to save minimum in the procedeure
#2 index is to save corresponding index of minimum
#3 temp is to transfer value for a[index] and a[i]