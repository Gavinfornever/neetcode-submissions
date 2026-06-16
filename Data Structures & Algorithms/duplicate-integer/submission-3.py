class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i, x in enumerate(nums):
            if x in dic: return True
            else: dic[x]=1
        return False