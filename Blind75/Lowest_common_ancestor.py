#TC:0(logn)
#SC:0(h)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #until the root is present
        #iterative approach
        while root != None:
            #if both the p and q values are smaller then the root value we are searching should be in the left
            if p.val < root.val and q.val < root.val:
                root = root.left
            #if both the p and q values are greater then the root value we are searching should be in the right
            elif p.val > root.val and q.val > root.val:
                root = root.right
            ##if not then the root is the answer
            else:
                return root
        #return the root when while is over
        return root
                