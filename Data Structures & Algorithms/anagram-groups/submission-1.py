class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        theMap = {}
        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str not in theMap:
                theMap[sorted_str] = [string]
            else:
                theMap[sorted_str].append(string)
        return list(theMap.values())
