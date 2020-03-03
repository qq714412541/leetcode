#def insertion_sort_divide(arr):




def compare(arr2,target,left,right):
    if right == left :
        if arr2[left] >= target:
            return arr2[:left] + [target] + arr2[left:]
        else:
            return arr2[:left+1] + [target] + arr2[left+1:]

    elif right-left ==1:
        if arr2[left] >= target:
            return arr2[:left] + [target] + arr2[left:]
        else:
            return arr2[:left+1] + [target] + arr2[left+1:]


    else:
        temp = (left+right)//2
        print(temp)
        if arr2[temp] == target:
            print(arr2[:2],[target,],arr2[8:])
            return arr2[:temp+1] + [target] + arr2[temp+1:]
        elif arr2[temp] > target:
            return compare(arr2,target,left,temp)
        elif arr2[temp] < target:
            return compare(arr2,target,temp,right)

arr2 = [0,1,2,3,4,5,6,7,9]
result = compare(arr2,-1,0,8)
print(result)

