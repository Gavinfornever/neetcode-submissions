class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # {1:1, 2:2, 3:3, 4:3}
        # {3:[3,4],2:[2],1:[1]}
        dic1 = {}
        dic2 = {}
        res = []
        for num in nums:
            dic1[num] = dic1.get(num, 0)+1
        for key, val in dic1.items():
            if val not in dic2:
                dic2[val] = []
            dic2[val].append(key)
        
        left = k
        freq = len(nums)
        while left!=0:
            if freq not in dic2:
                freq -=1
                continue
            tmp = dic2[freq]
            if len(tmp)>left:
                res = res+tmp[:left]
            else:
                res = res+tmp
                left -= len(tmp)
            freq -= 1
        return res


