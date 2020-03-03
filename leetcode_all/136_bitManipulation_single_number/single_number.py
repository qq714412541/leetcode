class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = set()
        #num.remove('a')
        for i in range(len(nums)):
            try:
                num.remove(nums[i])
            except:
                num.add(nums[i])
        return num.pop()


class Solution:#  x^x = x   0^x = x
    def singleNumber(self, nums: List[int]) -> int:
        temp = 0
        for i in nums:
            temp ^= i
        return temp
