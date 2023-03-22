#TC:0(n)
#SC:0(h)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
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
            level=[]
            #iterating the node to each level
            for i in range(size):
                #deleting the queue and adding it to node
                node=q.popleft()
                #appending each value to level array list
                level.append(node.val)
                #if the left node is present
                if node.left:
                    #then append it to the queue
                    q.append(node.left)
                if node.right:
                    #if node right is present then append it to queue 
                    q.append(node.right)
                    #adding the level arrays to result
            result.append(level)
        #returning the result
        return result