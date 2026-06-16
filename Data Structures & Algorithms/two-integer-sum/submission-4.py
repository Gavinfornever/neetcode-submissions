class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, x in enumerate(nums):
            table[target-x] = i
        
        for i, x in enumerate(nums):
            if x in table:
                if table[x] != i:
                    res = []
                    res.append(min(i, table[x]))
                    res.append(max(i, table[x]))
                    return res
        
        return -1