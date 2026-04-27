class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # find area, you loko at the heigh of both choose the lowest one andmultply that by the distance between the 2
        
        l = 0
        r = len(heights) - 1

        max_area = 0

        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            max_area = max(max_area, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return max_area
            

        



        
        