##find the standard
##narrow the range of the question to be suit for the standard
def sum(arr):
    total = 0
    for x in arr :
        total += x
    return total




def sum_new(arr): #recursion for the sum of elements in the array
    if arr == []:
        return 0
    else:
        return arr[0] + sum_new(arr[1:])

print(sum_new([1,2,3,4,5]))



def sum_count(array):#recursion for the number of elements in the array
    if array==[]:
        return 0
    else:
        return 1+sum_count(array[1:])


print(sum_count([1,1,1,2,1,3,4]))


def array_max(array):#recursion for finding maximum in the array
    a = int
    #temp = array[0]
    if array ==[]:
        return 0
    else:
        temp = array[0]
        if temp > array_max(array[1:]):
            a = temp

        else:
            a = array_max(array[1:])

        return a

print(array_max([1,2,3,4,5,6,5,3,2]))

