class Solution:
    def exchange(self, nums):
        i = 0
        j = 0
        while i <len(nums) and j<len(nums):
            if nums[i]%2==0:
                j=i+1
                while j<len(nums):
                    if nums[j]%2==1:
                        #x = nums[j]
                        nums[i+1:j+1],nums[i] = nums[i:j],nums[j]
                        j+=1
                        i+=1
                    else:
                        j+=1
            else:
                i+=1
        return nums

su = Solution()
arr = [1,2,3,4,5,6,7]
res = su.exchange(arr)
print(res)