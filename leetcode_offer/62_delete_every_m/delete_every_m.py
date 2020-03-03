class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if m == 1:
            return n-1
        #m = m%n
        cur = temp = Node(-1)
        for i in range(n):
            new_node = Node(i)
            temp.next = new_node
            temp = temp.next
        temp.next = cur.next
        ite = 0
        #t = 0
        count = 0
        while cur:
            if count == n-1:
                break
            while ite<m-1:
                cur = cur.next
                ite+=1
            cur.next = cur.next.next
            count+=1
            ite = 0

        return cur.val

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        arr = [i for i in range(n)]
        x = m
        while len(arr)>1:
            #print(arr)
            #print(m, len(arr))
            if m >len(arr):
                m = m%len(arr)
            #print(m)
            #arr.pop(m-1)
            arr = arr[m:]+arr[:m-1]
            m = x

        return arr[0]

su = Solution()
res = su.lastRemaining(10,17)
print(res)