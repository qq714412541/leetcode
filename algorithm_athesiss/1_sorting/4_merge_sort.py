def divide_conquer(arr,p,q,r):
    n1 = q-p +1
    n2 = r-q
    n3 = r-p+ 1
    #print(p,q,r,'input2')
    #print(n1,n2,n3,'range')
    left = []
    right = []
    for i in range(n1):
        #print(i)
        #print(i,p+i)
        #print(left[i],arr[0])
        left.append(arr[p+i])
    #print(left)
    for i in range(n2):
        #right[i] = arr[q+i+1]
        right.append(arr[q+i+1])
    left.append(float('inf'))
    right.append(float('inf'))
    #print(left,right)

    i = 0
    j = 0
    for k in range(n3):
        #print(k,'k')
        if left[i] > right[j]:
            arr[p+k] = right[j]
            j +=1
        else:
            arr[p+k] = left[i]
            i +=1

    return arr
arr= [1,3,5,7,9,2,4,6,8]
arr2 = [2,5]
arr3 = [4,5,3,7,5,1,4,6,9]
#result = divide_conquer(arr2,0,0,1)
#print(result)
#print(result)

#result = divide_conquer(arr,0,4,8)
#print(result)
import math
def merge_sort(arr,a,b):
    if a < b :
        temp = math.floor((b+a)/2)
        #print(a,temp,b)
        print(arr,'arr')
        #print(temp + 1, b, 'input')
        merge_sort(arr,a,temp)
        merge_sort(arr,temp+1,b)
        divide_conquer(arr, a, temp, b)

    else:
        return arr

    return arr


    return arr

result = merge_sort(arr3,0,8)
print(result)

#tips:
#1 middle equals to a+b  /2
#2 recursion happens before functional code!!!!   because when code is carried out to recursion, it will have priority to do recursion and at last it will
#run functional code one layer by one layer out!!!!