import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if not num in dic: dic[num] = 1
            else: dic[num]+=1
        heap = [(-val,key) for key, val in dic.items()]
        heapq.heapify(heap)
        print(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res