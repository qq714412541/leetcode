import numpy
class Solution:
    def findNumberIn2DArray(self, nums, target: int) -> bool:

        m = len(nums)
        if m == 0:
            return False
        #print(m)
        n = len(nums[0])
        #print(m,n)
        if n == 0:
            return False

        pivot = nums[m-1][0]
        #print(pivot)
        if target == pivot:
            return True
        elif target>pivot:
            #print('1111')
            if n == 1:
                return False
            else:
                nums = numpy.array(nums)
                nums = nums[:,1:]
                return self.findNumberIn2DArray(nums,target)
        elif target<pivot:
            #print('2222')
            if m == 1:
                return False
            else:
                return self.findNumberIn2DArray(nums[:m-1][:],target)
su = Solution()
arr = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]


res = su.findNumberIn2DArray(arr,-1)
print(res)