class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target > d * f:
            return 0
        temp = [1 for i in range(f)]
        res = []
        x = 1
        while x < d:
            ind = 0
            while ind < (x + 1) * f:
                count = 1
                t = 0
                while count <=f and ind - count >= 0:
                    if ind - count < x * f:
                        t += temp[ind - count]
                    count += 1
                res.append(t)
                ind += 1
            x += 1
            temp = res
            print(temp)
            res = []

        return temp[target - 1] % (10 ** 9 + 7)

su = Solution()
res = su.numRollsToTarget(2,6,7)
print(res)