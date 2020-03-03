class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        arr = [i for i in range(n)]
        ind = -1
        while arr:
            print(ind,'#')
            ind += m
            if ind>len(arr)-1:
                ind = ind%len(arr)-1
            x = arr.pop(ind)
            print(x)


su = Solution()
res  = su.lastRemaining(5,3)
print(res)