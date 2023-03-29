# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        
        # if not p and not q:
        #     return True



    #     p_values=[]
    #     q_values=[]
    #     self.recur(p,p_values)
    #     self.recur(q,q_values)
        
    #     return q_values== p_values
        
    # def recur(self,root,values):
        
    #     if root:
    #         values.append(root.val)
    #         print(values)
    #         self.recur(root.left,values)
    #         self.recur(root.right,values)
    #     else:
    #         values.append(None)


    #     # if not p and not q:
    #     #     return True
    #     # p_values=[]
    #     # q_values=[]    
    #     # self.recur(p)
    #     # self.recur(q)
    #     # return q_values==p_values

    #     # def recur(self,root,values):
    #     #     if not root:
    #     #         return 

    #     #     if not p or not q or p.val!=q.val:
    #     #         values.append(None)

    #     #     self.recur(root.left,values)
    #     #     self.recur(root.right,values)

