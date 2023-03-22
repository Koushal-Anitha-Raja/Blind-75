#TC:0(n)
#SC:0(h)
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #if root is null return empty array
        if not root:
            return []
        #create a queue and add the root to it
        q=deque()
        q.append(root)
        #initialize empty result array
        result=[]
        
        c = 0
        #until queu is empty
        while q:
            level=[]
            #size parameter for iterate through each step
            size=len(q)
            #print(size)
            #iterate through the size parameter each level 1 or 2 times
            for i in range (size):
                #pop out the value from queue and store it in a node variable
                node=q.popleft()
                #append the nodes value in lwvel 
                level.append(node.val)
                #if left node valid add it to queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    #if right node is present add it to queue
                    q.append(node.right) 

            #if the level is even append the result value directly  
                    
            if c%2==0:
                result.append(level) 
                #increment the counter value to one
                c+=1
            else: 
                #of the level is odd then reverse it and add it to the result
                result.append(level[::-1]) 
                #increment the counter value to one
                c+=1
                #return the result value
        return result
                