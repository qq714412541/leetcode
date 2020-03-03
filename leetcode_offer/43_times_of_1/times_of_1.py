class Solution:
    def countDigitOne(self, n: int) -> int:
        x = 1
        last = [0]
        temp = 1
        while n>=10**x:
            last.append(temp)
            temp +=(9*temp+10**(x))
            x+=1
        i=-1
        #n = n-10**(x-1)
        res = 0
        new = 0
        sign = 1
        while n>0:
            print(n,last[i],x)
            a,n = divmod(n,10**(x-1))
            x-=1
            if a == 0:
                if sign != 0:
                    new=last[i+1]
                    sign = 0

                else:
                    i-=1
                    continue
            elif a >1:
                new = last[i]*(a-1) +10**x
                sign = 1
            elif a ==1:
                if n == 0:
                    new = last[i]+1
                else:
                    new = (n+1)
                sign = 1
            print(new)

            i-=1
            res+=new
        return res


class Solution:
    def countDigitOne(self, n: int) -> int:
        divide = 1
        res = 0
        while n >=divide:
            high = n // (10 * divide)
            cur = n // divide - 10*high
            low = n - (high * 10 + cur) * divide

            #print(high,cur,low,divide)

            if cur == 0:
                res += (high * divide)
            elif cur == 1:
                res += (high * divide + low + 1)
            else:
                res += ((high + 1) * divide)
            #print(res)

            divide *= 10

        return res

su = Solution()
res = su.countDigitOne(561)
print(res)