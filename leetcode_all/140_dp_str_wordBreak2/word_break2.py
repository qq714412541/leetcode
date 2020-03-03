import copy
class Solution:
    def wordBreak(self, s: str, wordDict):
        dp = [True] + [False]*len(s)
        res = [[] for i in range (len(s) + 1)]

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j]:

                    if s[j:i] in wordDict:
                        #print(i, j, dp[j], s[j:i])
                        dp[i] = True
                        #print(res[i],res[j])
                        new = self.add(res[j],s[j:i])
                        #print(new,'?')
                        res[i] += new
                        #print(res[i])
                        print(res)
        #print(dp)
        #print(res)
        if dp[-1]:
            return res[-1]
        else:
            return []

    def add(self, arr, s):
        #print(arr,s,'###')
        new_arr = copy.deepcopy(arr)
        if new_arr:
            for i in range(len(new_arr)):
                new_arr[i]+=' ' + s
        else:
            new_arr+=[s]
        #print(new_arr,'###')

        return new_arr



su = Solution()

s = 'aaaaaaa'
arr = ["aaaa", "aaa"]

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
arr = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

res = su.wordBreak(s,arr)
print(res)

'''arr = ['aaa']
s = 'aaaa'
res = su.add(arr,s)
print(res)'''