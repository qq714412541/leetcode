class Solution:
    def maxPathSum(self, root) -> int:

        def re(node):
            if not node:
                return [0,float('-inf')]
            else:
                res_l = re(node.left)
                res_r = re(node.right)
                double_max = res_l[0]+res_r[0]+node.val
                single_max = max(res_l[0]+node.val,res_r[0]+node.val,node.val)
                all_max = max(double_max,single_max,res_r[1],res_l[1])
                res = [single_max,all_max]
                return res

        res = re(root)
        return res[1]