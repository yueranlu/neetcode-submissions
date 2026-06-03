class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # once a car catches upto anther ar that startted at  
        # further positio and sging slower than it, it has to drive along side it

        #when the positionof cars reach the target thay are finished
        # count hte numerof fleets/car in the ame position by the timet hey get to the fnihs line

        # use a stack to mainatin thetime of the flet as we interate throughthe arr  

        # add the seed a positio in pars into another array

        pairs = [(p, s) for p ,s in zip(position, speed)]
        pairs.sort(reverse = True)
        stack = []
        for p,s in pairs:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

            
