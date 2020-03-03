class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums = set(nums)
        cur_len =1
        max_len = 1
        for num in nums:
            if num-1 not in nums:
                while num+1 in nums:
                    num+=1
                    cur_len+=1
                    max_len = max(max_len,cur_len)
                cur_len = 1
            else:
                continue
        return max_len


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums = sorted(nums)
        max_len =1
        cur_len =1
        for i in range(1,len(nums)):
            #print(max_len,cur_len)
            if nums[i]-nums[i-1]==1:
                cur_len+=1
                max_len = max(max_len,cur_len)
            elif nums[i]==nums[i-1]:
                continue
            else:
                cur_len = 1
        return max_len