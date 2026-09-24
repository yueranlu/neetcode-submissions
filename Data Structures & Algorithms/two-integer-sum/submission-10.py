class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # take the first number, do target - number = check_num
        # if check_num not in the hashmap then we add number in the hashmap (key = number, value = index), then we keep going, once we find a value that is in the hashmap alr we return theindex of the 2
        checkedMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in checkedMap:
                return [checkedMap[diff], i]
            checkedMap[n] = i

        