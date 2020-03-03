class Solution:#wrong
    def wordBreak(self, s: str, wordDict) -> bool:
        start = 0
        end = 0
        while end < len(s):
            print(s[start:end+1])
            if s[start:end + 1] in wordDict:
                if end == len(s) - 1:
                    return True
                else:
                    start = end+1
            end += 1

        return False


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        x = list(set(s))
        y = list(set(''.join(i for i in wordDict)))
        print(x, y)
        #z = list(set(wordDict))
        for i in x:
            if i not in y:
                return False


        def search( s, arr, start, end):

            if start == end == len(s):
                return True
            while end < len(s):
                print(s[start:end + 1],start,end)
                if s[start:end + 1] in wordDict:
                    return  search(s, arr, end + 1, end + 1) or search(s, arr, start, end + 1)
                end += 1
            return False

        return search(s, wordDict, 0, 0)


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i,len(s)):
                if dp[i] and s[i:j+1] in wordDict:
                    #print(dp[i],s[i:j+1],i,j)
                    dp[j+1] = True
        #print(dp)
        return dp[-1]


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        dp = [True]
        for i in range(1,len(s)+1):
            dp += [any(dp[j] and s[j:i] in wordDict for j in range(i))]
            #print(dp,s[0:1])
        return dp[-1]


su = Solution()
s = "catsandog"
arr = ["cats", "dog", "sand", "and", "cat"]
#s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#arr = ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]
s = 'a'
arr = ['a']
res = su.wordBreak(s,arr)
print(res)