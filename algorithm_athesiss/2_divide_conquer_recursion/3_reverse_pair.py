global count
count = 0
def reverse_pair(arr,l,r):
    if l<r:
        mid = (l+r)//2
        reverse_pair(arr,l,mid)
        reverse_pair(arr,mid+1,r)
        sort(arr,l,r,mid)
    return arr

def sort(arr,l,r,mid):
    global count
    arr_l = arr[l:mid+1]
    arr_r = arr[mid+1:r+1]

    i = 0
    j = 0
    new_arr = []
    while i<=len(arr_l) and j<= len(arr_r):
        if i==len(arr_l):
            new_arr.extend(arr_r[j:])
            break
        elif j == len(arr_r):
            new_arr.extend(arr_l[i:])
            break
        elif arr_l[i] >arr_r[j]:
            count += len(arr_r[j:])
            print(arr_l[i:], arr_r[j:])
            new_arr.append(arr_l[i])
            i+=1
        else:
            new_arr.append(arr_r[j])
            j+=1
    for i in range(l,r+1):
        arr[i] = new_arr[i-l]
    return arr
arr = [3,1,5,2,2,0,9,8]
res = reverse_pair(arr,0,len(arr)-1)
#res2= merge(arr,0,3,1)
print(res)
print(count)