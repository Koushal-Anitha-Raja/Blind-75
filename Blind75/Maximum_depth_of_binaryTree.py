class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
    #bfs approach
        #if the root is not present return maxdepth as 0
        if not root:
            return 0
        #initially the depth is zero
        maxDepth = 0
        #adding the root value to queue
        q = deque()
        q.append(root)
  
        #until queue is empty do this
        while q:
            #size parameter for doing operations at each level
            size = len(q)
            #maxdepth is incremented to one as we traverse through each level
            maxDepth+=1
            #for each level run until both the left and rright node is present
            for _ in range(size):
                #first pop the node 
                node = q.popleft()
                #if left node is present append it to queue
                if node.left:
                    q.append(node.left)
                #if right node is present append it to queue
                if node.right:
                    q.append(node.right)
        #maxdepth has the maximum value of level 
        return maxDepth


        #dfs
        #assigning maxdepth initially to zero
        self.maxDepth = 0
        #passing the root and first level to the dfs function
        self.dfs(root,1)
        return self.maxDepth

    #recutrsice approach for each node to find the depth
    def dfs(self,root,depth):
        #base condition
        if not root:
            return

        #logic
        #maxdepth is the maximum between current depth and maximum depth
        self.maxDepth = max(depth,self.maxDepth)

        #if the node is in left subtree add one to the depth value
        self.dfs(root.left,depth+1)
  #if the node is in right subtree add one to the depth value
        self.dfs(root.right,depth+1)

