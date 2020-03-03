def insertion_sort(arr:list):
    temp = 0
    count = 0
    if len(arr) <= 1:
        return arr
    else:
        for i in range(1,len(arr)):
            for j in range(0,i):
                count += 1
                print(count)
                if arr[i-j] > arr[i-j-1]:
                    temp = arr[i-j]
                    arr[i-j] = arr[i-j-1]
                    arr[i-j-1] = temp
                else:
                    break
        return arr
    return arr


#x = insertion_sort([1,2,3,1,2,4,5,3,4,2,6,7,3])
#print(x)

#to make sure numbers behind are right, then a new number comes, we can compare it with the number behind it one by one.
#that needs two paremeters, the first is traversing for array and the second is the number what it needs to count--(0,i)
#waring!!!!!!!!: range(a,b) means form a to b-1   ... range(1,1) means nothing.

def insertion_sort_max(arr:list):
    temp = 0
    count = 0
    if len(arr) <= 1:
        return arr
    else:
        for i in range(1,len(arr)):
            print(i)
            for j in range(0,i):
                print(i,j)
                #print(j)
                if arr[i-j] > arr[i-j-1]:
                    temp = arr[i-j]
                    arr[i-j] = arr[i-j-1]
                    arr[i-j-1] = temp
                    #print(i,j,temp)
                else:
                    break
    return arr
    return arr

x = insertion_sort_max([3,2,3,1,2,4,5,3,4,2,6,7,3])
print(x)