def insertion_sort_recursion(arr):
    if len(arr)>=1:


        insertion_sort_recursion(arr[0: (len(arr)-1)])
        arr = compare(arr,arr[-1])
        print(arr,'result')
        return arr

    else:
        return arr
    return arr



def compare(arr,value):
    #new_arr = [0] * (len(arr))
    print(arr)
    for i in range(len(arr)-1):
        #print(i)
        if arr[i] > value:


            for j in range(0,len(arr)-i-1):
                print(i,j,len(arr)-i)
                #temp =
                #print(arr,j)
                arr[len(arr)-j-1] = arr[(len(arr)-j-2)]
                print(arr[len(arr)-j-1],arr[(len(arr)-j-2)])
                #temp = arr[j]
                #arr[j] = arr[j + 1]
                #arr[j+1] = temp

            #arr[]
            arr[i] = value
            print(arr)

            #arr[i] = value

            #new_arr[i] = value
            #new_arr[i+1:] = arr[i+1:]

        #else:
            #new_arr[i] = arr[i]
    return arr#new_arrarr

arr = [1,5,3,6,3,6,7,4,3,9]
result = insertion_sort_recursion(arr)
print(result)