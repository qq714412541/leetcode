#time complexity = O(n*logn)
def maxstrMid(arr:list,low,mid,high):
    #leng = len(arr)
    left_sum = float('-inf')
    suml = 0
    for i in range(0,mid - low +1):
        suml = suml + arr[mid - i]
        if left_sum < suml:
            left_sum = suml     #left_sum equal to maximum from mid to low
            #print(left_sum)
            l_index = mid - i     #index is what sum corresponds to


    right_sum = float('-inf')
    sumr = 0
    for j in range(1,high - mid+1):
        sumr = sumr + arr[mid+j]
        if right_sum < sumr:
            right_sum = sumr
            #print(j,mid+j,right_sum)
            r_index = mid + j


    return l_index,r_index,right_sum+left_sum



#a,b,c = maxstrMid(arr,0,4,9)
#print(a,b,c)

import math
def maxsubstr(arr:list,low,high):
    #leng = len(arr)
    if low >=high:
        return low,high,arr[low]
    else:
        mid = math.floor((low+high)/2)

        l_low,l_high,l_sum = maxsubstr(arr,low,mid)

        r_low,r_high,r_sum = maxsubstr(arr,mid+1,high)

        al_low,al_high,al_sum = maxstrMid(arr,low,mid,high)

        print(l_sum,r_sum,al_sum)
        print(l_low,l_high,l_sum,'#')


        if l_sum >= al_sum and l_sum>= r_sum:
            return l_low,l_high,l_sum
        elif r_sum >= al_sum and r_sum>= l_sum:
            return r_low,r_high,r_sum
        elif al_sum >= l_sum and al_sum>=r_sum:     #consistent bigger than sign can not exist because that can not hold all situations.
            return al_low,al_high,al_sum
arr = [3,-4,2,5,-4,-4,5,-3,5,-7,6,9,-4,5]
a, b, c = maxsubstr(arr, 0, 6)
print(a, b, c)


#tips:
#1 divide question into three parts, find maximum in left ,find maximum in right, find maximum between left and right(when the edge of left and
# right have been known)
#2 do recursion in def. when get into recursion, we do recursion to minimize the range of array.
#3 when do recursion, it will finally comes to find maximum between left and right
#4 in fact, what we do is to find the maximum one by one with the edge becoming bigger.(idea of recursion)
#5 whats more. the parameters we input needs to have edge because that can help us do recursion to minimize teh edge
#6 range(low,high) mid=floor((sum)/2), when take place of parameters, low = mid+1,high = mid. thus we can add end situation
#when low ==high
#arr1 = [-5, -6, -7, -8, -5, -3, -4]