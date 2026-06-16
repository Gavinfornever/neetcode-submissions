class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table_s = {}
        table_t = {}
        for i, x in enumerate(s):
            if x not in table_s:
                table_s[x] = 1
            else:
                table_s[x] += 1
        for i, x in enumerate(t):
            if x not in table_t:
                table_t[x] = 1
            else:
                table_t[x] += 1
        # set_s = set(table_s)
        # set_t = set(table_t)
        return table_s == table_t