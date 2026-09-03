class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            tuple_count = tuple(count)
            if tuple_count not in dic:
                dic[tuple_count] = []
            dic[tuple_count].append(s)
        return list(dic.values())
