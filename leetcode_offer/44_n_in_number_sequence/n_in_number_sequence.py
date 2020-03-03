class Solution:
    def findNthDigit(self, n: int) -> int:
        if n == 0:
            return 0
        #n = n+1
        x = 1
        last = 0
        temp = 9
        while n>temp:
            x+=1
            last = temp
            temp+=(x*9*10**(x-1))
        tar = n - last
        print(n,last)
        a,b = divmod(tar,x)
        print(a,b)
        #return 3
        if a == 0:
            if b ==1:
                return 1
            else:
                return 0
        new = 10**(x-1) + a
        print(new)
        if b == 0:
            return int(str(new-1)[-1])
        else:
            return int(str(new)[b-1])
su = Solution()
res = su.findNthDigit(15)
print(res)