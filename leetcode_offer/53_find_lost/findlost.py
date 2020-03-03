class Solution:
    def missingNumber(self, nums) -> int:
        l = 0
        r = len(nums)
        while l<r:

            mid = l+(r-l)//2
            print(l, r,mid)
            if nums[mid]>mid:
                r = mid
            else:
                l = mid+1

        return l
su = Solution()
arr = []
res = su.missingNumber(arr)
print(res)