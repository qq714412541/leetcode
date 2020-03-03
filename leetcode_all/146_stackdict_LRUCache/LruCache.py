#import queue
class LRUCache:# implemented by array

    def __init__(self, capacity: int):
        self.que = []
        #self.queue = queue.Queue()
        self.dict = {}
        self.max = capacity
        self.count = 0

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        else:
            index = self.que.index([key,self.dict[key]])
            self.que.pop(index)
            self.que.append([key,self.dict[key]])
            return self.dict[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.dict.keys():
            if self.count < self.max:
                self.que.append([key, value])
                self.dict[key] = value
                self.count += 1
                print(self.dict)
            else:
                #if key not in self.dict.keys():
                #print(self.que)
                new = [key, value]
                out = self.que.pop(0)
                #print(out,self.que,self.dict)
                self.dict.pop(out[0])
                self.que += [new]
                self.dict[key] = value
                print(self.dict)
        else:
            old = self.dict[key]
            if old != value:
                self.dict[key] = value
                index = self.que.index([key,old])
                self.que.pop(index)
                self.que.append([key,value])
                #self.que[index] = [key,value]

["LRUCache","put","put","get","put","put","get"]
[[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]

su = LRUCache(2)

su.put(2,1)
su.put(2,2)
print(su.get(2))
su.put(1,1)
#print(su.get(2))
su.put(4,1)
#su.put(5,'b')

#print(su.get(5),':b')
print(su.get(2))
#print(su.get(3))
#print(su.get(4))
#print(su.get(2),':-1')
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


'''class LRUCache:# implemented by linkedlist

    def __init__(self, capacity: int):
        self.max =capacity
        self.count = 0
        self.head = Node(0)
        self.dict = {}

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        else:
            new_node = Node(0)
            new_node.next = self.head.next
            while new_node.next:
                if new_node.next.val == [key,self.dict[key]]:
                    new_node.next = new_node.next.next
            new_node.next = Node([key,self.dict[key]])
            return self.dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            new_node = Node(0)
            new_node.next = self.head.next
            while new_node.next:
                if new_node.next.val == [key, self.dict[key]]:
                    new_node.next = new_node.next.next
            new_node.next = Node([key, value])
            self.dict[key] = value
        else:
            if self.count<self.max:
                '''


