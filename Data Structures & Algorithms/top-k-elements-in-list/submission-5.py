import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buc = [[] for _ in range(len(nums)+1)]
        dic = {}
        for i, x in enumerate(nums):
            dic[x] = 1 + dic.get(x,0)
            # if x not in dic:
            #     dic[x] = 1
            # else:
            #     dic[x] += 1
        for num, count in dic.items():
            buc[count].append(num)

        res = []
        count = k
        for x in reversed(buc):
            for y in x:
                if count!=0: 
                    res.append(y)
                    count-=1

        return res