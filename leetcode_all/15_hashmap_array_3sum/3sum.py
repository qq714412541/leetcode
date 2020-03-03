class Solution:
    def threeSum(self, nums):

        nums = sorted(nums)


        res = []
        while nums and nums[0]<=0 and [0,0,0] not in res:

            i=0

            target = -nums[i]
            #print(i,target,operate1)
            nums.pop(i)

            res  += self.twosum(nums,target)
            #print(res1)
        dic = list(set([tuple(t) for t in res]))
        dic = [list(v) for v in dic]

        return dic

    def twosum(self,arr, target):
        #print(arr,target)
        #print(arr,target)
        table = {}
        solution = []
        for i in range(len(arr)):
            if arr[i] in table.keys():
                #print(arr[i])
                #print(arr[i],table.keys())
                solution.append([-target,arr[i], target - arr[i]])

            val = target - arr[i]
            table[val] = i
        return solution

su=Solution()
arr= [-1,-1,0,0,0,1,1]
res = su.threeSum(arr)
print(res)
