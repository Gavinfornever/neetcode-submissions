class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, x in enumerate(nums):
            dic[target-x] = i
        for i, x in enumerate(nums):
            if x in dic.keys() and i!=dic[x]:
                res = []
                res.append(min(i, dic[x]))
                res.append(max(i, dic[x]))
                return res