#TC:0(n)
#SC:0(h)
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return []
        
        
        q=deque()
        #append the root value to queue
        q.append(root)
        #having a result variable 
        result=[]
        
        while q:
            #using the size parameter for each level
            size=len(q)
            level=[]
            #iterating through the each level to find nodes at each level
            for i in range(size):
                #deleting the node value from queue
                node=q.popleft()
                #appending the node values to each level
                level.append(node.val)
                
                #as they are multiple childrens 
                for child in node.children:
                    #then append the child to queue
                    q.append(child)
                    #appending all the array values to result
            result.append(level)
            
        #returning the result array    
        return result