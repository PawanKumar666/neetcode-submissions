class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n
        left = 1
        right = 1
        for i in range(n): # accumulating left products
            result[i] *= left
            left *= nums[i]
        for i in range(n-1, -1, -1): # accumulating right products
            result[i] *= right
            right *= nums[i]
        return result

        
        