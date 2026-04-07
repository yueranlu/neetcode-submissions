class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #have a lsit for the result with the same length as the og list
        res = [1]*len(nums)

        #set prefix to 1 to start multiplying
        prefix = 1

        # make a for loop and for each number in the list add the prefix to the index inthe resultlist
        for i in range(len(nums)):
            res[i]  = prefix
            prefix *= nums[i] #this will multiply by the next nuber in the list each tie always pdating the prefix
        # now set post fix to 1
        postfix = 1
        # now loop backwards and multiply each index in the result list byt the resulting postfix
            #update the postfix by 
        for i in range(len(nums) -1 , -1 , -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res



        