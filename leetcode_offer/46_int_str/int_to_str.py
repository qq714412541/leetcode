class Solution:
    def translateNum(self, num: int) -> int:
        global res
        res = 0
        num = str(num)
        temp = {
            '0': 'a',
            '1': 'b',
            '2': 'c',
            '3': 'd',
            '4': 'e',
            '5': 'f',
            '6': 'g',
            '7': 'h',
            '8': 'i',
            '9': 'j',
            '10': 'k',
            '11': 'l',
            '12': 'm',
            '13': 'n',
            '14': 'o',
            '15': 'p',
            '16': 'q',
            '17': 'r',
            '18': 's',
            '19': 't',
            '20': 'u',
            '21': 'v',
            '22': 'w',
            '23': 'x',
            '24': 'y',
            '25': 'z',
        }
        self.back(num,temp,'')
        return res
    def back(self,cur,temp,last):
        global res
        if not cur:
            res+=1
        elif len(cur) == 1:
            last += temp[cur]
            self.back('',temp, last)
        else:
            x1 = temp[cur[0]]
            self.back(cur[1:],temp,last+x1)
            if cur[0:2] in temp.keys():
                self.back(cur[2:],temp,last+temp[cur[0:2]])

su = Solution()
res = su.translateNum(12258)
print(res)

