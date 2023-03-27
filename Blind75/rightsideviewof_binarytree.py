# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:  
        #bfs method
        #if the root is not present 
        if not root:
            return []
        
        q=deque()
        #appending the root values  to queue
        q.append(root)
        
        #a new result array for storing result
        result=[]
        while q:
            #to find the each level we ned to find the size
            size=len(q)
            #iterating the node to each level
            for i in range(size):
                #deleting the queue and adding it to node
                node=q.popleft()
                #if the left node is present
                if node.left:
                    #then append it to the queue
                    q.append(node.left)
                if node.right:
                    #if node right is present then append it to queue 
                    q.append(node.right)
                    #adding the node value to result
            result.append(node.val)
    
        #returning the result
        return result
        
        
    #      """ #dfs method
    #     #assigning the result array
    #     self.ans = []
    #     #the recursion fun will take root and 0
    #     self.recur(root, 0)
    #     #returning the result
    #     return self.ans
    
    # #dfs function
    # def recur(self, node,i):
    #     #if not is not present
    #     if not node:
    #         return
        
    #     #if the length is equal to i
    #     if i == len(self.ans):
    #         #then add the node val to each array
    #         self.ans.append(node.val)
    #         #add the right side tree first and left side tree next
    #     self.recur(node.right, i+1)
    #     self.recur(node.left, i+1)
    #     """