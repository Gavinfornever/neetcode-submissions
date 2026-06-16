class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        print(count)
        maxHeap = [ [-cnt, num] for num, cnt in count.items() ]
        heapq.heapify(maxHeap)
        res = []
        for _ in range(k):
            cnt, num = heapq.heappop(maxHeap)
            res.append(num)
        return res


