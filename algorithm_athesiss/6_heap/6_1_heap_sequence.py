def max_heap(arr:list,index):
    left = 2*(index+1)-1
    right = 2*(index+1) +1-1

    if left <= len(arr) and arr[index] < arr[left]:
        largest = left
    else:
        largest = index



    if right <= len(arr) and arr[largest] < arr[right]:
        largest = right




    if largest != index:
        temp = arr[index]
        arr[index] = arr[largest]
        arr[largest] = temp
        max_heap(arr,largest)


####this part can only find arr[index]'s maximum, that means to keep attributes of heap(parent is bigger than childs)

import math
def build_heap(arr:list):
    leng = len(arr)
    for i in range(math.floor(leng/2)):
        max_heap(arr,len-i)

