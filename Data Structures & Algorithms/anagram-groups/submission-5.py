from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i, s in enumerate(strs):
            count = [0]*26
            for j, c in enumerate(s):
                count[ord(c)-ord('a')] += 1
            dic[tuple(count)].append(s)
        
        res = []
        for val in dic.values():
            res.append(val)
        return res