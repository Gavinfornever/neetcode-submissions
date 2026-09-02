class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        res = []
        for i, num in enumerate(nums):
            dic[num] = i
        
        for i, x in enumerate(nums):
            if target-x in dic and dic[target-x]!=i:
                res.append(i)
                res.append(dic[target-x])
                return res