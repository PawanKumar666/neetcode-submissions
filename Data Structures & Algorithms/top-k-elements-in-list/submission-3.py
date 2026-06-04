from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        theMap = defaultdict(int)
        for num in nums:
            theMap[num] += 1
        return [val[0] for val in sorted(theMap.items(), key=lambda x: x[1], reverse=True)[:k]]
            

        