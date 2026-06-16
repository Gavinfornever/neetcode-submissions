class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, x in enumerate(nums):
            table[x] = i
        
        for i, x in enumerate(nums):
            if (target-x) in table and table[target-x]!=i:
                return [min(i, table[target-x]), max(i, table[target-x])]