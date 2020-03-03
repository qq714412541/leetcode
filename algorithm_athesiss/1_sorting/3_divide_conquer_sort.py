def divide_conquer(arr,p,q,r):
    n1 = q-p +1
    n2 = r-q
    n3 = r-p+ 1
    #print(n1,n2,n3)
    left = []
    right = []
    for i in range(n1):
        print(i)
        #print(i,p+i)
        #print(left[i],arr[0])
        left.append(arr[p+i])
    print(left)
    for i in range(n2):
        #right[i] = arr[q+i+1]
        right.append(arr[q+i+1])
    left.append(float('inf'))
    right.append(float('inf'))

    i = 0
    j = 0
    for k in range(n3):
        if left[i] > right[j]:
            arr[p+k] = right[j]
            j +=1
        else:
            arr[p+k] = left[i]
            i +=1

    return arr


#tips:
#1 as for list. blank list can not directly be valued as left[i]  because index is out of list. for cycle, we can use append to add value
#or we can new a list with lengh
#2 range(0,n) is number for 0~n-1, (1,n) is number of 1 and n.
#3 set a sentinel of inf to compare
#4 if we do not use sentinel, we can set judgement to judge whether the count number equals to length. when them equal, we can put the rest
#directly into array

def divide_conquer2(arr,p,q,r):
    n1 = q-p +1
    n2 = r-q
    n3 = r-p+ 1
    #print(n1,n2,n3)
    left = []
    right = []
    for i in range(n1):
        print(i)
        #print(i,p+i)
        #print(left[i],arr[0])
        left.append(arr[p+i])

    for i in range(n2):
        #right[i] = arr[q+i+1]
        right.append(arr[q+i+1])
    print(left, right)
    #left.append(float('inf'))
    #right.append(float('inf'))

    i = 0
    j = 0
    for k in range(n3):
        print(i,j,k,len(left)-1,len(right)-1)

        if i==len(left)-1:
            arr[p+k:] = right[j:]
            break
        elif j==len(right)-1:
            arr[p+k:] = left[i:]
            break

        if left[i] > right[j]:
            arr[p+k] = right[j]
            j +=1
        else:
            arr[p+k] = left[i]
            i +=1

    return arr

arr= [1,3,5,7,9,2,4,6,8]

result = divide_conquer2(arr,0,4,8)
print(result)