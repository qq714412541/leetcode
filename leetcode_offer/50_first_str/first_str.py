class Solution:
    def firstUniqChar(self, s: str) -> str:
        temp = {}
        for t in s:
            if t not in temp:
                temp[t] = 1
            else:
                temp[t] = temp[t]+1
        for key,val in temp.items():
            if val == 1:
                return key
        return ' '