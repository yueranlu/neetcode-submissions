class Solution:
    def trap(self, height: List[int]) -> int:

        # find the amount of water that can be trapped in each column
        # for each colmn check the blocka around it, if it is higher then the ones around it then it can;t have water
        l = 0
        r = len(height) - 1
        water = 0
        lMax = height[l]
        rMax = height[r]

        while l < r:
            if lMax < rMax:
                l+=1
                lMax = max(lMax, height[l])
                water += lMax - height[l] #minuus the tallest wall on the elft so far from the currernt height[l]
            else:
                r-=1
                rMax = max(rMax,height[r])
                water += rMax - height[r]
        
        return water

         




        