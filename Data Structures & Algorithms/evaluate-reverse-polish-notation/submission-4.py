class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    
        # once you get to an operation symbol 
        # do it without the number you have stored and the precious number

        # loop thrgouh the list, keep tack of the numbers in a stack
        # once you encounter an operation symbol, you perform the operation onthe numbes in the stack
        # there should be max 2 numebs in the stack at all times



        stack = []

        for i in tokens:
            if i not in '+-/*':
                stack.append(int(i))
            elif i == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
            elif i == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif i == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 * num2)
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))
        return stack[0]







        

        