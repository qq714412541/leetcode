class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif x == 0:
            return 0


        sign = -1 if n%2==1 and x<0 else 1
        x=abs(x)
        #print(sign,n,n%2)
        if n <0:
            x = 1/x
            n=-n

        #print(x,n,'?')

        count = 1
        ini = x
        #count_all = 0
        res = x
        while count <= n:
            #print(count, ini)
            if count == n:

                return res*sign
            count_new = count + count
            if count_new > n:
                n -=count
                count = 1
                ini = x
                res *= ini
            else:
                res*=ini
                ini_new = ini * ini
                count = count_new
                ini = ini_new
            #print(count,ini,n,res,'#')


su = Solution()
res = su.myPow(5,0)
print(res)