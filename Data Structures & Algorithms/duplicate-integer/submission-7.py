class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sn = set()
        for num in nums:
            if num in sn:
                return True
            sn.add(num)
        return False

   
