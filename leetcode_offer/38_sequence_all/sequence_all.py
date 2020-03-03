class Solution:
    def permutation(self, s: str):
        ''.split(s)
        print(s)
        s = list(set(s))
        print(s)
        res = []
        def re(temp,last,rest):
            if not rest:
                temp.append(last)
            for i in range(len(rest)):
                #print(temp,last,rest[i],rest[:i],res[i+1:])
                re(temp,last+rest[i],rest[:i]+rest[i+1:])
        re(res,'',s)
        return res

su = Solution()
res = su.permutation('aabcd')
print(res)