class Solution:
    def minNumber(self, nums) -> str:
        nums = self.qsort(nums)
        return nums





    def qsort(self,arr):
        print(arr)
        if len(arr)>=2:
            pivot = arr[0]
            l = []
            r = []
            for a in arr[1:]:
                if a < pivot:
                    l.append(a)
                else:
                    r.append(a)
            print(l, r)
            return self.qsort(l)+[pivot]+self.qsort(r)
        else:
            return arr





su = Solution()
arr = [5,2,6,8,4,6,3,5,7,8]
res = su.minNumber(arr)
print(res)