class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dic = {}

        def getDict(s):
            d = {}
            for c in s:
                d[c] = d.get(c, 0)+1
            return d 

        for s in strs:
            s_dict = getDict(s)
            tmp = tuple(sorted(s_dict.items()))
            if tmp not in dic:
                dic[tmp] = []
            dic[tmp].append(s)

        for x in dic.values():
            res.append(x)
        
        return res

