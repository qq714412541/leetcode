class Solution:
    def minNumber(self, nums) -> str:
        max_n = max(nums)
        l = len(str(max_n))
        rank = {}
        for num in nums:
            num = str(num)
            for x in num:
                if int(x) > int(num[0]):
                    rank_num = int(num + (l - len(num)) * num[0]) - 0.5
                    break
                else:
                    rank_num = int(num + (l - len(num)) * num[0]) + 0.5
                    break
            rank[num] = rank_num

        res = sorted(rank.items(), key=lambda x: x[1])
        print(res)
        ret = ''
        for r in res:
            ret += r[0]

        # res = ''.join(res[i for i in range(res)][0])
        return ret


class Solution:
    def minNumber(self, nums) -> str:
        for num in nums:
            num = str(num)
        res = self.merge(nums, 0, len(nums))
        res = ''.join(res)
        return res

    def merge(self, arr, l, r):
        print(l,r)
        if l< r:
            mid = (l + r) // 2
            l_part = self.merge(arr, l, mid)
            r_part = self.merge(arr, mid+1, r)
            arr = self.q_sort(l_part + r_part)
            return arr
        else:
            return arr

    def q_sort(self, arr):

        l = []
        r = []
        pivot = arr[0]
        for a in arr:
            if a + pivot < pivot + a:
                l.append(a)
            else:
                r.append(a)
        res = l + [pivot] + r
        print(res,'#')
        return res


class Solution:
    def minNumber(self, nums) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        nums = self.qsort(nums)
        return ''.join(nums)

    def qsort(self,nums):
        if len(nums) >= 2:
            l = []
            r = []
            piv = nums[0]
            for a in nums[1:]:
                if a + piv < piv + a:
                    l.append(a)
                else:
                    r.append(a)

            return self.qsort(l) + [piv] + self.qsort(r)
        else:
            return nums


su = Solution()
arr = [12,121]
res = su.minNumber(arr)
print(res)