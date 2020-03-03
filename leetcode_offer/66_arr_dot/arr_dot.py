class Solution:
    def constructArr(self, a):
        l = []
        temp = 1
        for i in range(len(a)):
            temp*=a[i]
            l.append(temp)
        temp = 1
        res = []
        #print(l)
        for i in range(len(a)):
            #print(temp)
            if i <= len(a)-2:
                res = [temp*l[len(a)-i-2]] + res
            else:
                res = [temp] + res
            temp*=a[len(a)-i-1]
        return res

class Solution:
    def constructArr(self, a):
        l = []
        temp = 1
        for i in range(len(a)):
            temp*=a[i]
            l.append(temp)
        temp = 1
        res = []
        #print(l)
        for i in range(len(a)-1,-1,-1):
            if i == 0:
                res = [temp]+res
            else:
                res = [temp*l[i-1]] + res
            temp *= a[i]
        return res


class Solution:# initial arr instead of append
               #because append will use more time!!!!!
    def constructArr(self, a):
        res = [0 for i in range(len(a))]
        # l = []
        temp = 1
        for i in range(len(a)):
            res[i] = temp
            temp *= a[i]

        temp = 1

        # print(l)
        for i in range(len(a) - 1, -1, -1):
            res[i] *= temp
            temp *= a[i]

        return res

su = Solution()
arr = [1,2,3,4,5]
res = su.constructArr(arr)
print(res)