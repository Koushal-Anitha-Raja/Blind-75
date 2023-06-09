class Solution:
    def coinChange(self, coins, amount):
#         result=[]
        
#    #first iterating numbe rof columns and the initial amount is 0 and intitializing a dp array
#         dp=[[ 0 for _ in range (amount+1)] for _ in range(len(coins)+1)]
         
#          #base condition
#          #filling all the colums with infinity
#         for j in range (1,amount+1):
#             dp[0][j]=amount+1 #this is infinity

#      # 1 is already done so ,iterate the row and then iterate through column
#         for i in range (1,len(coins)+1):
#             for j in range (amount+1):
#              #choose the no choose scenario until the value is different
#                  if j<coins[i-1]:
#                     #copy the previous row value of same column
#                      dp[i][j]=dp[i-1][j]
                

#                  else:
#                         #coin change logic to choose the min possiblity coins to select
#                         dp[i][j]=min(dp[i-1][j], 1+dp[i][j-coins[i-1]])

#         if dp[-1][-1]==amount+1 :#infinity case
#             return -1

            
#         i = len(coins)
#         j = amount
#         while i>0:
#             #no choose
#             if dp[i][j] == dp[i-1][j]:
#                 i=i-1
#             #choose
#             else:
#                 result.append(coins[i-1])
#                 j=j-coins[i-1]


        
   #first iterating numbe rof columns and the initial amount is 0 and intitializing a dp array
        dp= [ float("inf") for j in range(amount+1) ]
        dp[0] =0
         
         #base condition
         #filling all the colums with infinity
       
        for i in range(1,amount+1):
     # 1 is already done so ,iterate the row and then iterate through column
            for coin in coins:

             #choose the no choose scenario until the value is different
                if i<coin:
                    #copy the previous row value of same column
                    continue
                else:
                    #coin change logic to choose the min possiblity coins to select
                    dp[i]=min(dp[i], 1+dp[i-coin])

    
        if dp[amount]==float("inf"):#infinity case
            return -1
        else:
            return dp[amount]      
            
        

#         if sum(result) == amount:
#             return len(result)   


        