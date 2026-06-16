class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """opst: [""]"""
        table = {}
        for i, x in enumerate(strs):
            m = ''.join(sorted(x))
            if m not in table:
                table[m] = []
            table[m].append(x)
        
        res = []
        for x in table.values():
            res.append(x)

        return res


