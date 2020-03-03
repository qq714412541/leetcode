
def kConcatenationMaxSum( arr, k: int):
    mod = 10**9 + 7
    sum1 = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            sum_temp = sum(arr[i:j])
            if sum_temp > sum1:
                sum1 = sum_temp

    if max(arr) <= 0:
        return 0
    else:
        if k==1:

            return sum1 % mod

        elif k >= 2:
            sum_arr = sum(arr)
            max_left = 0
            for i in range(len(arr)):
                sum_temp = sum(arr[i:])
                if sum_temp > max_left:
                    max_left = sum_temp

            max_right = 0
            for i in range(len(arr)):
                sum_temp = sum(arr[:(len(arr) - i)])
                if sum_temp > max_right:
                    max_right = sum_temp
            if sum_arr>0:
                sum2 = max_left + max_right + (k - 2) * sum_arr
            else:
                sum2 = max_left + max_right
            print(max_left,max_right)
            print(sum1,sum2)

            return max(sum1, sum2) % mod

x = kConcatenationMaxSum([-9,13,4,-16,-12,-16,3,-7,5,-16,16,8,-1,-13,15,3],6)
print(x)