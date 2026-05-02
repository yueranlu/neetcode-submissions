class Solution:
    def isValid(self, s: str) -> bool:
      # stack is just an array
      stack = []
      pairs = {')': '(', ']':'[', '}':'{' }


      # loop thru array and add every open bracket to the stack
      # when encountering a closed bracket check if it matches the latest bracket in the stack
      # if yes then remove the bracket off the stack and continue
      # if no return false



      for b in s:
         if b in pairs:
            if stack and stack[-1] == pairs[b]:
               stack.pop()
            else: 
               return False
         else:
            stack.append(b)
      if stack:
         return False
      else:
         return True

   
            


         

