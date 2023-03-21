#TC:0(n)
#SC:0(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #assign left and right pointers to zero and first position
        l,r=0,1
        #assign maxprofit as zero 
        maxprofit=0
        #iterate through until right pointer is less than lenght of prices
        while r<len(prices):
            #profitable
            if prices[r]>prices[l]:
                #assign profit variable as prices of right minus left pointers
                profit=prices[r]-prices[l]
                #compare maxprofit with maxprofit and profit and assign it to maxprofit
                maxprofit=max(maxprofit,profit)
            #if not profitable
            else:
                #left pointer equals to right
                l=r
            #increment right to right plus one
            r=r+1    
         #return the maxprofit    
        return maxprofit    
                
                
        
        
