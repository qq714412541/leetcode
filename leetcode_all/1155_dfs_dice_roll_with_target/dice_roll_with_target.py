import time


def singleton(func):
    def count(*args):
        a = time.time()
        res = func(*args)
        b = time.time()
        print('time:',b - a)
        return res

    return count
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        global res
        res = 0
        self.re(d, f, target)
        mod = 10**9 +7
        return res%mod

    def re(self, d, f, target):
        #print(d,f,target)
        if f >= target and d == 1 and target > 0:
            global res
            res += 1
            print(res)
        elif d > 1:
            for i in range(1, f + 1):
                if i + (d-1)*f>target and target-i>0:

                    self.re(d - 1, f, target - i)
        else:
            return


class Solution:
    @singleton
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d * f < target:
            return 0
        global mem
        mem = {}
        res = self.re(d, f, target)
        mod = 10 ** 9 + 7
        return res % mod

    def re(self, d, f, target):

        if d == 1 and target <= f and target > 0:
            return 1
        elif d>1:

            global mem
            # print(mem)
            cur = 0
            for i in range(1, f + 1):
                if (d - 1, target - i) in mem:
                    cur += mem[(d - 1, target - i)]
                else:
                    if target - i >= 0:
                        temp = self.re(d - 1, f, target - i)
                        mem[(d - 1, target - i)] = temp
                        cur += temp
            return cur
        else:
            return 0





class Solution:
    @singleton
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d*f<target:
            return 0
        elif f*f == target:
            return 1

        global mem
        mem = {}

        res = self.re(d, f, target)
        mod = 10**9 +7
        return res%mod

    def re(self, d, f, target):
        if d == 1 and target>0 and target<=f:
            return 1
        elif d>1:
            global mem
            res = 0
            for i in range(1,f+1):
                if (d-1,target-i) in mem:
                    res+=mem[(d-1,target-i)]
                else:
                    if target-i>0:
                        temp = self.re(d-1,f,target-i)
                        mem[(d-1,target-i)] = temp
                        res+=temp
                    else:
                        continue
            return res
        else:
            return 0
su = Solution()
res = su.numRollsToTarget(30,30,500)
print(res)


