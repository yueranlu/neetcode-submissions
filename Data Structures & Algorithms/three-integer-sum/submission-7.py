class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # 2 pointers, one that iterates from left to tightm and one from right to elft 
        nums.sort()
        res = []

        # for each 
        for i, a in enumerate(nums):
            if a > 0: # if a is bigger thatn 0, then iti impossiel for the three numers to be 0
                break

            if i > 0 and a == nums[i - 1]:
                continue # this avoid dupliactes, it check if this number is the sam eas the last number that you are checking,
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if a + nums[l] + nums[r] > 0:
                    r -= 1
                elif a + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    r -= 1 
                    while nums[l] ==nums[l-1] and l < r:
                        l += 1      
           
        return res



        