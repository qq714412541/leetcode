import copy
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ini = []
        dot = [2,3,5]
        new_ini = [1]

        while len(new_ini)<n:
            temp = copy.deepcopy(new_ini)
            #print(ini,new_ini)
            for do in dot:
                for i in range(len(ini),len(new_ini)):
                    new_ini.append(new_ini[i]*do)
            ini = temp

            print(new_ini,'?')
            new_ini = list(set(new_ini))
            new_ini.sort()
            #new_ini = list(set(new_ini.sort()))
            #new_ini.sort()
            print(new_ini,'#')
        return new_ini[n-1]

su = Solution()
res = su.nthUglyNumber(10)
print(res)