class Solution:
    def kConcatenationMaxSum(self, arr, k: int) -> int:
        model = 10**9 +7
        max_mid = self.find_max_mid(arr)
        max_l = self.find_max_left(arr)
        max_r = self.find_max_right(arr)
        sum_arr = sum(arr)
        print(max_mid,max_l,max_r,sum_arr)

        if max_mid ==0:
            return 0
        else:
            if k ==1:
                return max_mid%model
            else:
                if sum_arr <=0:
                    return max(max_mid,max_l + max_r) % model
                else:
                    return max(max_mid,max_l+max_r+(k-2)*sum_arr) %model





    def find_max_mid(self,s):


        sum_m = 0
        max_sum = 0
        for i in range(len(s)):
            if s[i]>=0 or sum_m + s[i]>0:
                sum_m +=s[i]
                max_sum = max(max_sum,sum_m)
            else:
                sum_m = 0
        return max_sum

    def find_max_left(self,s):
        max_sum = 0
        sum_l = 0
        for i in range(len(s)):
            sum_l += s[i]
            max_sum = max(sum_l,max_sum)
        return max_sum

    def find_max_right(self,s):
        max_sum = 0
        sum_l = 0
        for i in range(len(s)):
            sum_l += s[len(s)-i-1]
            max_sum = max(sum_l, max_sum)
        return max_sum


su = Solution()
arr = [-16,-14,18,14,-17,-6,9,13,10,-5,-15,-3,15,11,-1,-10,-10,-9]
res = su.kConcatenationMaxSum(arr,12)
print(res)