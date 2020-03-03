class Solution:
    def isStraight(self, nums) -> bool:
        nums = sorted(nums)
        while len(nums)>1:
            if nums[-2] == nums[-1]-1:
                nums.pop()
            elif nums[0] == 0:
                nums.pop(0)
                nums[-1]-=1
            else:
                return False
        return True

su = Solution()
arr = [1,2,3,4,5]
res = su.isStraight(arr)