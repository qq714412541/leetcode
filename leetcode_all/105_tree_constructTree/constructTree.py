# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        cur = TreeNode(0)
        self.construct(preorder, inorder, 'l', cur)
        return cur.left

    def construct(self, pre_, in_, dire, node):
        if pre_:
            # print(node.val,pre_)
            new_node = TreeNode(pre_[0])
            if dire == 'l':
                node.left = new_node
            else:
                node.right = new_node

            root_val = pre_[0]
            index = in_.index(root_val)
            left_in = in_[:index]
            right_in = in_[index + 1:]
            l = len(left_in)
            left_pre = pre_[1:1 + l]
            right_pre = pre_[1 + l:]

            self.construct(left_pre, left_in, 'l', new_node)
            self.construct(right_pre, right_in, 'r', new_node)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:#将两个合成一个的想法
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            #print(preorder,inorder)
            root = preorder[0]
            node = TreeNode(root)
            #print(node.val)
            index = inorder.index(root)
            pre_l = preorder[1:1+index]
            pre_r =preorder[1+index:]
            in_l = inorder[:index]
            in_r =inorder[index+1:]
            node.left = self.buildTree(pre_l,in_l)
            node.right = self.buildTree(pre_r,in_r)
            #print(node.left.val,node.right.val)
            return node

