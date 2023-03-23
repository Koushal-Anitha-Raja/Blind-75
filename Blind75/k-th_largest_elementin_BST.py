
#TC:0(n)
#SC:0(h)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #initialize the k value
        self.k=k
        #resultant variable to store the output
        self.result=0
        #recursiv function 
        self.dfs(root)
        return self.result
       
#recursive function which has only root as parameter
    def dfs(self,root):
        #if the root is not present then unfold the recursion
        if not root :
            return 

        #traverse through the left subtree    
        self.dfs(root.left)
        #decrease k value by one at each instance
        self.k-=1
        #if k is equal to zero then the k the smallest element is acheived
        if self.k==0:
            #assign the k th value to the result 
            self.result=root.val
        #as it is inorder traversal we are processing left ,root and then right
        self.dfs(root.right)
