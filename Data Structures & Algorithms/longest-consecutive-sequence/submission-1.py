from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        minNum = float('inf')
        maxNum = float('-inf')
        for x in nums:
            dic1[x] = dic1.get(x,0)+1
            minNum = min(minNum, x)
            maxNum = max(maxNum, x)
        print(dic1)
        p = minNum + 1
        dic2[minNum] = 1
        while p<=maxNum:
            if p not in dic1:
                p+=1
                continue
            if (p-1 not in dic2):
                dic2[p] = dic2.get(p,0)+1
            else:
                dic2[p] = dic2[p-1]+1
            print(p, dic2[p])
            p+=1

        # for x in nums:
        #     if x in dic2:
        #         continue
        #     if x-1 in dic2:
        #         dic[x] = dic[x-1]+1
        #     else:
        #         dic[x] = 1
        
        return max(dic2.values())
