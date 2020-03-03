from queue import LifoQueue


class Solution:
    def isBalanced(self, root) -> bool:
        if not root:
            return True
        myqueue = LifoQueue()
        myqueue.put(root)
        judge = True
        while not myqueue.empty() and judge:
            node = myqueue.get()
            if node.left:
                myqueue.put(node.left)
            if node.right:
                myqueue.put(node.right)
            judge = self.height(node)
        return judge

    def height(self, node):
        if node.left:
            height_l = self.checked(node.left, 1)
        else:
            height_l = 0
        if node.right:
            height_r = self.checked(node.right, 1)
        else:
            height_r = 0
        if abs(height_l - height_r) > 1:
            return False
        else:
            return True

    def checked(self, node, count):
        if node.left and node.right:
            return max(self.checked(node.left, count + 1), self.checked(node.right, count + 1))
        elif node.left and not node.right:
            return self.checked(node.left, count + 1)
        elif node.right and not node.left:
            return self.checked(node.right, count + 1)
        else:
            return count



class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

#from queue import LifoQueue


class Solution:#best answer
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        h, judge = self.checked(root)

        return judge

    def checked(self, node):
        # print(count)
        if node.left and node.right:
            h_l, ba_l = self.checked(node.left)
            h_r, ba_r = self.checked(node.right)
            # print(max(h_l,h_r), ba_l , ba_r , abs(h_l-h_r)<=1,node.val )
            return max(h_l, h_r) + 1, ba_l and ba_r and abs(h_l - h_r) <= 1
        elif node.left and not node.right:
            h_l, ba_l = self.checked(node.left)
            # print(h_l, ba_l , h_l<=1,node.val,'#')
            return h_l + 1, ba_l and h_l == 0
        elif node.right and not node.left:
            h_r, ba_r = self.checked(node.right)
            # print(h_r, ba_r , h_r<=1,node.val,'###')
            return h_r + 1, ba_r and h_r == 0

        else:
            return 0, True
