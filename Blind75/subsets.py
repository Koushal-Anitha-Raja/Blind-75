class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        #using for loop method
         # the resultant array
        result = [[]]
        #iterate through the nums array
        for num in nums:
            #size variable for each level
            size = len(result)
            for i in range(size):
                # assigning the result of i value in the temp 
                temp = result[i][:] 
                temp.append(num)
                #appending the value to temp
                result.append(temp) 

        #the final result array        
        return result 
        
        
        
        
        
       #using backtrack 
        self.nums=nums
        self.result=[]
        self.backtrack(0,[])
        return self.result
    
    def backtrack(self,pivot,path):
        self.result.append(path[:])
        
        for i in range(pivot,len(self.nums)):
            #action
            path.append(self.nums[i])
            #recursion
            self.backtrack(i+1,path)
            
            #backtrack
            path.pop()
            
            
            #using choose no choose
        self.nums = nums # declaring the nums
        self.result = [] # creating the resultant array
        self.backtrack(0,[]) # calling the backtrack function recursively with 0 and empty array
        return self.result # returning the result
    
    def backtrack(self,i,subset):
        if i == len(self.nums): # if i is equal to length of nums
            self.result.append(subset[:]) # appending the subset array into result
            return
        
        self.backtrack(i+1,subset) # calling backtrack function with incrementing i by 1
        subset.append(self.nums[i]) # appending the nums of ith element to subset array
        self.backtrack(i+1,subset) # calling backtrack function with incrementing i by 1
        
        subset.pop() # popping the subset array
        
        
        #choooe nochoose
        self.nums = nums # declaring the nums
        self.result = [] # creating the resultant array
        self.backtrack(0,[]) # calling the backtrack function recursively with 0 and empty array
        return self.result # returning the result
    
    def backtrack(self,i,subset):
        if i == len(self.nums): # if i is equal to length of nums
            self.result.append(subset[:]) # appending the subset array into result
            return
        
        self.backtrack(i+1,subset) # calling backtrack function with incrementing i by 1
        subset.append(self.nums[i]) # appending the nums of ith element to subset array
        self.backtrack(i+1,subset) # calling backtrack function with incrementing i by 1
        
        subset.pop() # popping the subset array