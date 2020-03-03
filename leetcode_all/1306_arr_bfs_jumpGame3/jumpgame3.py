class Solution:
    def canReach(self, arr, start: int) -> bool:
        global temp
        global judge
        judge = False
        temp = {}
        # temp[start] = start
        self.jump(arr, start)
        return judge

    def jump(self, arr, start):
        global temp
        temp[start] = start
        print(start)
        x = arr[start]
        if x == 0:
            global judge
            judge = True
            return
        else:
            if start + x <= len(arr) - 1 and start + x not in temp.keys():
                self.jump(arr, start + x)
            if start - x >= 0 and start - x not in temp.keys():
                self.jump(arr, start - x)

import queue
class Solution2:
    def canReach(self, arr, start: int) -> bool:
        myque = queue.Queue()
        visited = set()

        myque.put(start)

        while not myque.empty():
            x = myque.get()
            print(x)
            if arr[x] == 0:
                return True
            if x not in visited:
                visited.add(x)
                for i in (x - arr[x], x + arr[x]):
                    if i >= 0 and i <= len(arr) - 1:
                        myque.put(i)

        return False

su = Solution2()
arr = [0]
start = 0
res = su.canReach(arr,start)
print(res)