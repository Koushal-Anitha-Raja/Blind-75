class Solution:
    def maxArea(self, height: List[int]) -> int:
        low=0
        #as the height value starts from zero
        right= len(height)-1
        
        #declaring a max variable for sum
        max_area=0
        #iterate through until left crosses right
        while(low<right):
            #calculating area by area = lenght and breath (here breath is choosen as minimum as it it the higher bound for the container )
            max_area=max(max_area, min(height[low],height[right]) *(right-low))
            #if the left pointer is low move left pointer by one
            if height[low]<height[right]:
                low+=1
            else:
                #else just move the right pointer 
                right-=1
                #print the mx_area which has largest area value
        return max_area
    
#time complexity:0(n)
#space complexity:0(1)