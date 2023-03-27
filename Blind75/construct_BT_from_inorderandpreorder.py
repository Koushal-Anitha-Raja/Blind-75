class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #if the node isnot present return null
        if not preorder or not inorder:
            return None
        #creating a treenode with root as value
        root=TreeNode(preorder[0])
        #finding a pivot element
        for i in range(len(inorder)):
            if inorder[i]==root.val:
                pivot=i
                #calling the main function as left and right parameters
        root.left=self.buildTree(preorder[1:pivot+1],inorder[:pivot])

        root.right=self.buildTree(preorder[pivot+1:],inorder[pivot+1:])
        #finally return the root
        return root