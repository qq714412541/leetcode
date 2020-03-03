

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == q:
            return True
        elif p ==None or q == None:
            return False
        else:



            myqueue1 = queue.Queue()
            myqueue2 = queue.Queue()
            myqueue1.put(p)
            myqueue2.put(q)

            while not myqueue1.empty() and not myqueue2.empty():
                a = myqueue1.get()
                b = myqueue2.get()

                #if a == b and (myqueue1):
                if a == None and b ==None:
                    continue

                if a == None or b == None:
                    return False


                if a.val != b.val:
                    return False

                else:
                    myqueue1.put(a.left)
                    myqueue1.put(a.right)
                    myqueue2.put(b.left)
                    myqueue2.put(b.right)
            return True


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if p == None and q == None:
            return True
        if p == None or q==None:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)