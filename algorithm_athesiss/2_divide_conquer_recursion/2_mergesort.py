#def mergesort(arr,l,r):
def mergesort(arr,l,r):
    #print(arr)
    if l<r:
        mid = (l+r)//2
        mergesort(arr,l,mid)
        mergesort(arr,mid+1,r)


        #print(l,r)
        merge(arr,l,r,mid)
    return arr



def merge(arr,l,r,m):
    arr_l = arr[l:m+1]
    arr_r = arr[m+1:r+1]

    i = 0
    j = 0
    new_arr = []
    while i<=len(arr_l) or j<=len(arr_r):
        if i == len(arr_l):
            new_arr.extend(arr_r[j:])
            break
        elif j == len(arr_r):
            new_arr.extend(arr_l[i:])
            break
        elif arr_l[i] < arr_r[j]:
            new_arr.append(arr_l[i])
            i+=1
        else:
            new_arr.append(arr_r[j])
            j+=1
        #print(new_arr)
    for i in range(l,r+1):
        arr[i] = new_arr[i-l]
    #print(arr)
    return arr


arr = [3,1,5,2,2,0,9,8]
res = mergesort(arr,0,len(arr)-1)
#res2= merge(arr,0,3,1)
print(res)