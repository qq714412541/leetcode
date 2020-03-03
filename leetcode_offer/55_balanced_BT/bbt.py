class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        res,deep = self.re(root,1)
        return res


    def re(self,node,deep):
        if not node:
            return True,deep-1
        else:
            #print()
            l,deepl = self.re(node.left,deep+1)
            r,deepr = self.re(node.right,deep+1)
            return abs(deepl-deepr)<=1 and l and r, max(deepl,deepr)
