class Solution:
    def findContinuousSequence(self, target: int):
        l = 1
        r = target
        res = []
        temp = 0
        while l<=r:
            arr = [i for i in range(l,r+1)]
            print(sum(arr),l,r,temp)
            if sum(arr) == target:
               res.append(arr)
            elif sum(arr) >target:
                temp+=l
                if temp>r:
                    r-=1
                    temp =0
                else:
                    l+=1
            else:
                return res
class Solution:
    def findContinuousSequence(self, target: int):
        mid = target//2
        res = []
        l1 = mid
        r1 = mid
        while l1>=1 and l1<=r1:
            arr = [i for i in range(l1,r1+1)]
            if sum(arr)>target:
                r1-=1
            elif sum(arr) == target:
                res.append(arr)
                r1-=1
            else:
                l1-=1
        l2 = mid
        r2 = mid
        while r2<target and l2<=r2:

            arr = [i for i in range(l2,r2+1)]
            #print(arr,l2,r2)
            if sum(arr)<target:
                r2+=1
            elif sum(arr) == target:
                res.append(arr)
                break
            else:
                break
        res = sorted(res,key= lambda x:x[0])
        return res

class Solution:
    def findContinuousSequence(self, target: int):
        mid = target//2
        res = []
        l = 1
        r = 1
        while l<=r and l<=mid:
            arr = [i for i in range(l,r+1)]
            if sum(arr) == target:
                res.append(arr)
                l+=1
            elif sum(arr)<target:
                r+=1
            else:
                l+=1
        return res


class Solution:###improved!!!!!!!!
    def findContinuousSequence(self, target: int):
        mid = target // 2
        res = []
        l = 1
        r = 1
        cur_sum = 1
        while l <= r and l <= mid:
            print(l,r,cur_sum)
            if cur_sum == target:
                res.append([i for i in range(l,r+1)])
                cur_sum -= l
                l += 1

            elif cur_sum < target:

                r += 1
                cur_sum += r
            else:
                cur_sum -= l
                l += 1
        return res

su = Solution()
res = su.findContinuousSequence(1)
print(res)