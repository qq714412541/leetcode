class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=1
        #temp = set()
        max_len = 1
        while i<len(s) and j<=len(s):
            cur = s[i:j]
            print(cur)
            print(cur[-1])
            print(cur[:-1])
            print('##')
            if cur[-1] not in cur[:-1]:
                #temp.add(cur)
                max_len = max(max_len,j-i)
                j+=1
            else:
                i = i + cur.index(cur[-1])+1
                j+=1
            #print(i,j)
        return max_len
su =Solution()
res = su.lengthOfLongestSubstring('ax')
print(res)