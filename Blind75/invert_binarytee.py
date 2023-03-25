# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #if the root node is not present
        if not root:
            return 
        self.recur(root)
        return root
    #recursive method of root     
    def recur(self,node):
        if node == None:
            return 
        #either you can do pre order or post order but not inorder because the root can be changed and inverted or inverted and roots can be changed
        self.recur(node.left)
        self.recur(node.right)
        # postorder
        node.left,node.right=node.right,node.left