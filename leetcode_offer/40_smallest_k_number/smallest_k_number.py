class Solution:
    def getLeastNumbers(self, arr, k: int):
        if k >= len(arr):
            return arr
        myheap = maxheap()
        for i in range(k):
            myheap.shift_up(arr[i])
        for i in range(k, len(arr)):
            myheap.shift_up(arr[i])
            myheap.shift_down()
        return myheap.heap


class maxheap:
    def __init__(self):
        self.heap = []

    def shift_up(self, x):
        self.heap.append(x)
        l = len(self.heap)
        s = l - 1
        while s > 0:
            if self.heap[s] > self.heap[(s - 1) // 2]:
                self.heap[s], self.heap[(s - 1) // 2] = self.heap[(s - 1) // 2], self.heap[s]
                s = (s - 1) // 2
            else:
                break

    def shift_down(self):
        x = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        l = len(self.heap)
        s = 0
        while s <= (l - 2) / 2:
            if 2 * s + 2 < l:
                if self.heap[s] < self.heap[2 * s + 1] or self.heap[s] < self.heap[2 * s + 2]:
                    if self.heap[2 * s + 2] > self.heap[2 * s + 1]:
                        self.heap[s], self.heap[2 * s + 2], = self.heap[2 * s + 2], self.heap[s]
                        s = 2 * s + 2
                    else:
                        self.heap[s], self.heap[2 * s + 1], = self.heap[2 * s + 1], self.heap[s]
                        s = 2 * s + 1
                else:
                    break
            else:
                if self.heap[s] < self.heap[2 * s + 1]:
                    self.heap[s], self.heap[2 * s + 1], = self.heap[2 * s + 1], self.heap[s]
                    s = 2 * s + 1
                else:
                    break

su = Solution()
arr = [0,1,1,1,4,5,3,7,7,8,10,2,7,8,0,5,2,16,12,1,19,15,5,18,2,2,22,15,8,22,17,6,22,6,22,26,32,8,10,11,2,26,9,12,9,7,28,33,20,7,2,17,44,3,52,27,2,23,19,56,56,58,36,31,1,19,19,6,65,49,27,63,29,1,69,47,56,61,40,43,10,71,60,66,42,44,10,12,83,69,73,2,65,93,92,47,35,39,13,75]
k = 75
#arr = [1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,7,7,8]
res = su.getLeastNumbers(arr,k)
print(res)

a = [0,0,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,4,5,5,5,6,6,6,7,7,7,7,7,8,8,8,8,9,9,10,10,10,10,11,12,12,12,13,15,15,16,17,17,18,19,19,19,19,20,22,22,22,22,23,26,26,27,27,28,29,31,32,33,35,36,39,40,42]

print(len(res),len(a))
for i in range(75):
    if res[i] in a:
        #print(len(a))
        #print(res[i])
        #print(a)
        a.remove(res[i])

    else:
        continue
print(res)
print(a)