def quicksort(arr):  #firstly, choose a standard for 1_sorting, and divide array to three parts: arr1(whose elements are smaller), [standard],arr2
    if len(arr) < 2:# then do recursion in arr1 and arr2, finally, we can get a new array which is sorted
        return arr
    else:
        arr1 = []
        arr2 = []

        standard = arr[0]
        for ele in arr[1:]:
            if ele < arr[0]:
                arr1 += [ele]

            else:
                arr2 += [ele]

        return quicksort(arr1) + [standard] + quicksort(arr2)

#print(quicksort([1,0,2,3,2,7,0,2,3,6,7,0]))


#in the worst situation, time complexity is O(n^2). But  it tends to be O(n*logn) in average


#recursion!


def quicksort2(arr,l,r):

    if l>r:
        return
    else:
        i=l
        j=r
        pivot = arr[l]

        while i<j:
            while i<j and arr[j]>=pivot:

                j-=1
            arr[i]=arr[j]#
            #print(j)
            while i<j and arr[i]<=pivot:
                i+=1
            arr[j]=arr[i]#
        arr[i] = pivot
        #print(arr)
        print(arr[l:i],arr[i+1:r+1],arr[i])
        quicksort2(arr,l,i-1)
        quicksort2(arr,i+1,r)






def quicksort3(arr,l,r):#wrong!!! our pivot is left, if we do iteration form left, the right one will be lost

    if l>r:
        return
    else:
        i=l
        j=r
        pivot = arr[l]

        while i<j:
            while i<j and arr[i]<=pivot:
                i+=1
            arr[j]=arr[i]#
            print(arr,'#')
            while i<j and arr[j]>=pivot:
                j-=1
            arr[i]=arr[j]#
            print(arr,'##')
        arr[j] = pivot
        quicksort3(arr,l,j-1)
        quicksort3(arr,j+1,r)



def quicksort4(arr,l,r):#if we set right to be pivot, then we can do iteration from left

    if l>r:
        return
    else:
        i=l
        j=r
        pivot = arr[r]

        while i<j:
            while i<j and arr[i]<=pivot:
                i+=1
            arr[j]=arr[i]#
            print(arr,'#')
            while i<j and arr[j]>=pivot:
                j-=1
            arr[i]=arr[j]#
            print(arr,'##')
        print(j,'?')
        arr[j] = pivot
        quicksort4(arr,l,j-1)
        quicksort4(arr,j+1,r)

data = [2,1,2,0,1,2,0,1,2]
quicksort2(data, 0, len(data) - 1)
print(data)
