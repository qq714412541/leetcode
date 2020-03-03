class Solution:
    def singleNumbers(self, nums):
        temp = 1
        for num in nums:
            temp ^= num
        temp ^= 1
        count = 0
        while temp & 1 != 1:
            #print(temp)
            temp >>=1
            count += 1
        tar = 2 ** count
        temp1 = 1
        temp2 = 1

        for num in nums:
            if num & tar == tar:
                temp1 ^= num
            else:
                temp2 ^= num
        temp1 ^= 1
        temp2 ^= 1
        return [temp1, temp2]
su = Solution()
arr = [1,2,10,4,1,4,3,3]
res = su.singleNumbers(arr)
print(res)




