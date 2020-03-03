import math
def twodivide_search(arr,target,left,right):
    #temp = math.floor((temp+len(arr)-1)/2)
    #if temp
    if left >right:
        return False
    #elif arr[-1] == target:
        #return len(arr)-1
    else:
        temp = (left+right)//2
        print(right,temp)

        if arr[temp] == target:
            return temp
        elif arr[temp] < target:
            #twodivide_search(arr[0:temp],target)
            return twodivide_search(arr,target,temp+1,right)
        elif arr[temp] > target:
            return twodivide_search(arr,target,left,temp-1)


arr = [1,2,3,4,5,6,7,8,9]
res = twodivide_search(arr,9,0,8)
print(res)

###tips:
#1 add a comparation to set a threshold to judge whether the comparation is over the array.
#then we get a comparation between left and right, we do not need equal sign as that can be used in edge.
#such as when left and right both equal to 8 or 0
#2 we need to set a standard to recursion. then we will think that which is changed in each recursion?
#answers are two edges, and the mid value is change by them.
# if we only input value temp. it will only cover one edge, because // is math.floor, we it becomes bigger than or equal to arr[-1]
# left will no longer be bigger. and the recursion will not stop.