import queue
class Solution:#BFS
    def levelOrder(self, root):
        myqueue = queue.Queue()
        res = []
        myqueue.qsize()

        myqueue.put(root)
        while not myqueue.empty():
            x = myqueue.get()
            res.append(x.val)
            if x.left:
                myqueue.put(x.left)
            if x.right:
                myqueue.put(x.right)
        return res