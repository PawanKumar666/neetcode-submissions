class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        crossed = {}
        for i, num in enumerate(nums):
            if target - num in crossed:
                return [crossed[target-num], i]
            crossed[num] = i
        