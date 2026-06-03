class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        crossed = {}
        for i in range(len(nums)):
            if target - nums[i] in crossed:
                return [crossed[target-nums[i]], i]
            crossed[nums[i]] = i
        