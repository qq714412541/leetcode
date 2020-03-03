class Solution:
    def minArray(self, numbers) -> int:

        ind = self.bi_search(numbers, 0, len(numbers))
        #print(ind)
        return min(numbers[0], numbers[ind])

    def bi_search(self, numbers, l, r):
        if l < r:
            mid = (l + r) // 2
            res = self.is_res(numbers, mid)
            #print(res)
            if res != 0:
                return res
            else:
                #print(l,mid,r)
                return self.bi_search(numbers, l, mid) + self.bi_search(numbers, mid + 1, r)
        else:
            return 0

    def is_res(self, nums, i):
        #print('###')
        if i < len(nums) and i > 0:
            if nums[i - 1] > nums[i]:
                return i
            else:
                return 0
        else:
            return 0


class Solution:#全闭[]
    def minArray(self, numbers) -> int:
        if len(numbers)==1:
            return numbers[0]
        res = self.bi_re(numbers, 0, len(numbers)-1)
        #print(res,'#')
        return numbers[res]

    def bi_re(self, numbers, l, r):
        if l < r:
            mid = (l + r) // 2
            #print(l,r,mid,numbers[mid],numbers[r])
            if numbers[mid] > numbers[r]:
                return self.bi_re(numbers, mid+1, r)
            elif numbers[mid] < numbers[r]:
                return self.bi_re(numbers, l, mid)
            else:
                return self.bi_re(numbers, l, r - 1)
        else:
            #print(l,r)
            return r

class Solution:#全闭[]
    def minArray(self, numbers) -> int:
        l = 0
        r = len(numbers)-1
        while l<r:
            mid = (l+r)//2
            if numbers[mid]>numbers[r]:
                l = mid+1
            elif numbers[mid]<numbers[r]:
                r = mid
            else:
                r-=1
        return numbers[r]




class Solution:
    def max(self,number):
        l=0
        r=len(number)-1
        while l<r:
            if l == r-1:
                return max(number[l],number[r])
            mid = (l+r)//2
            print(l,r,mid)
            if number[mid]>number[l]:
                l = mid
            elif number[mid]<number[l]:
                r = mid-1
            else:
                l+=1
        #return number[l]



class Solution:#双闭的时候，需要保证能取到r所以终止边界为l<=r
    def find(self,number,v):
        l=0
        r=len(number)-1
        while l<=r:
            mid = (l+r)//2
            if number[mid] == v:
                return mid
            elif number[mid]>v:
                r = mid-1
            else:
                l = mid+1
        return -1
su =Solution()
arr = [1,2,3,4,5,6,7,8,9]
tar = 10
res = su.find(arr,tar)
print(res)