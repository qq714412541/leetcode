class Solution:
    def maxSlidingWindow(self, nums, k: int):
        l = 0
        r = k
        res = []
        while r<=len(nums):
            print(l,r,nums[l:r])
            res.append(max(nums[l:r]))
            l+=1
            r+=1
        return res


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        if not nums:
            return []
        l = 0
        r = k
        cur_max = max(nums[l:r])
        res = []
        while r <= len(nums)-1:
            #print(cur_max,l,r)
            res.append(cur_max)
            l += 1
            r += 1
            if nums[l-1] == cur_max:
                cur_max = max(nums[l:r])
                #print(cur_max,l,r)
            elif nums[l-1] < cur_max:
                #print(r,len(nums))
                cur_max = max(cur_max, nums[r-1])
        res.append(cur_max)

        return res

su = Solution()
arr = [1,-1]
k = 1
res = su.maxSlidingWindow(arr,k)
print(res)