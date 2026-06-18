class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = [0]*len(height)
        rightmax = [0]*len(height)
        total_water = 0
        for i in range(len(height)):
            if i == 0:
                leftmax[i] = height[i]
            else:
                leftmax[i] = max(height[i], leftmax[i-1])
        for i in range(len(height)-1,-1,-1):
            if i == len(height)-1:
                rightmax[i] = height[i]
            else:
                rightmax[i] = max(height[i], rightmax[i+1])
        # rightmax.reverse()
        for i in range(len(height)):
            if i == 0 or i == len(height)-1:
                continue
            else:
                total_water += min(leftmax[i], rightmax[i]) - height[i]

        return total_water
        
        
            
        