class Solution:
    def isValid(self, s: str) -> bool:
        
        # check indexes of the list fromt he first one
        # keep track of already done brackets in the stack
        # Then would you encounter a close bracket make sure the open is the latest onein the stack, if it istthen stack and loop on

        stack = []

        pairs = {']':'[', '}':'{', ')':'('} 

        for b in s:
            if b in pairs:
                if stack and stack[-1] == pairs[b]:
                    stack.pop()
                    continue
                else: 
                    return False  
            else:
                stack.append(b)
        if not stack:
            return True
        else:
            return False
 
                        


                