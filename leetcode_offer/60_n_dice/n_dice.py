class Solution:
    def twoSum(self, n: int):
        x = 1
        temp = [1,1,1,1,1,1]
        res = []
        while x<n:
            ind = 0
            while ind<6*(x+1):
                #print(ind,'###')
                count = 1
                t = 0
                while count<=6 and ind - count >=0:
                    #print(temp)
                    if ind-count <6*x:
                        #print(ind-count)
                        #print(ind-count)
                        t+=(temp[ind-count])
                    count+=1

                #print(ind,t)
                res.append(t)
                ind+=1
            x+=1
            temp = res
            print(temp)
            res = []

            #print(temp,res)


        return list(filter(lambda a: a!=0,map(lambda a:a/(6**n),temp)))

su = Solution()
res = su.twoSum(2)
print(res)