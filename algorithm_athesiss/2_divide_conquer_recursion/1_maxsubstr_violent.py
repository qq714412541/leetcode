def substr_violent(arr):
    leng = len(arr)
    sum_compare = float('-inf')
    #temp = 0
    #count = 0
    for i in range(0,leng):
        for j in range(1,leng-i+1):
            #count +=1
            temp = sum(arr[i:i+j])
            if temp > sum_compare:

                sum_compare = temp
                low = i
                high = i+j-1
                print(temp,i,j)

    return low,high,sum_compare#,count

arr = [3,-4,2,5,-4,-4,5,-3,5,-7,6,9,-4,5]

print(substr_violent(arr))
