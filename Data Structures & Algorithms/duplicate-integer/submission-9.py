class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        listSet = set()
        for num in nums:
            if num in listSet:
                return True
            listSet.add(num)
        return False


        