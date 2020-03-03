class Solution:
    def reversePairs(self, nums) -> int:
        global res
        res = 0
        self.merge(nums, 0, len(nums) - 1)
        return res

    def merge(self, arr, l, r):
        if l < r:
            mid = (l + r) // 2
            self.merge(arr, l, mid)
            self.merge(arr, mid + 1, r)
            self.sort(arr, l, r,mid)

    def sort(self, arr, l, r, m):
        arr_l = arr[l:m + 1]
        arr_r = arr[m + 1:r + 1]
        new = []
        i = 0
        j = 0
        #print(arr_l,arr_r,l,m,m+1,r)
        while i <= m - l + 1 and j <= r - m:
            #print(i,j,m-l+1,r-m+1)
            global res
            if i == m - l+1:
                new.extend(arr_r[j:])
                break
            elif j == r - m:
                new.extend(arr_l[i:])
                # global res
                #print(m-l+1-i,'1111111')
                #res += (m - l - i)
                break
            elif arr_l[i] > arr_r[j]:
                new.append(arr_r[j])
                #print(j+1,'2222222222')
                res +=  (m-l-i+1)
                j += 1
            else:
                new.append(arr_l[i])
                i += 1
        #print(res,'##')
        arr[l:r + 1] = new

su = Solution()
arr = [2,1,0]
res = su.reversePairs(arr)
print(res)






