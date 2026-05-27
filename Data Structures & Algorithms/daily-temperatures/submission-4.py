class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        #loop through each elemnt
            # if it's the first elemnt= stack is emptu, add it to the stack
            # while loop
                # within the while loop for each number tat isnot reate than it add it to the stack


        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((temp,i))
        return res





            
        