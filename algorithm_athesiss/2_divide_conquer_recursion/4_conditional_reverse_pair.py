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
            for k in range(len(arr_r[j:])):
                if arr_l[i] > 2* arr_r[j]:

                    count += 1
                    print(arr_l[i:], arr_r[j:])
                else:
                    break
            new_arr.append(arr_l[i])
            i+=1
        else:
            new_arr.append(arr_r[j])
            j+=1
    for i in range(l,r+1):
        arr[i] = new_arr[i-l]
    return arr
'''arr = [3,1,5,2,2,0,9,8]
res = reverse_pair(arr,0,len(arr)-1)
#res2= merge(arr,0,3,1)
print(res)
print(count)'''

import bisect
class Solution:
    def reversePairs(self, nums) -> int:
        #print(2**31)
        global count
        count = 0
        return self.reverse_pair(nums, 0, len(nums) - 1)

    def reverse_pair(self, arr, l, r):
        global count
        if l < r:
            mid = (l + r) // 2
            self.reverse_pair(arr, l, mid)
            self.reverse_pair(arr, mid + 1, r)
            self.sort(arr, l, r, mid)
        return count

    def sort(self, arr, l, r, mid):
        #print(l,r)
        global count
        arr_l = arr[l:mid + 1]
        arr_r = arr[mid + 1:r + 1]
        #print(arr_l,arr_r)

        i = 0
        j = 0
        new_arr = []
        while i <= len(arr_l) and j <= len(arr_r):
            #print('$')
            if i == len(arr_l):
                new_arr.extend(arr_r[j:])
                break
            elif j == len(arr_r):
                new_arr.extend(arr_l[i:])
                break
            elif arr_l[i] > arr_r[j]:
                position = bisect.bisect_right(arr_r[j:],arr_l[i]/2)
                #if position < len(arr_r[j:]):
                count+=len(arr_r[j:])-position
                print(count)

                #print(i)
                new_arr.append(arr_l[i])
                i += 1
            elif arr_l[i]<0 and arr_r[j]>=arr_l[i] and arr_l[i] > 2 * arr_r[-1]:
                count+=1
                #print(i)
                new_arr.append(arr_r[j])
                j += 1
            else:

                # print(i,arr_r[j])
                new_arr.append(arr_r[j])
                j += 1
        for i in range(l, r + 1):
            arr[i] = new_arr[i - l]
        return arr




su = Solution()
arr = [2147483647,2147483647,-2147483647,-2147483647,-2147483647,2147483647]
res = su.reversePairs(arr)
print(res)