from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if length%2!=0:return False

        dic = {
            # '[':']',
            ']':'[',
            # '(':')',
            ')':'(',
            # '{':'}',
            '}':'{',
        }
        q = deque()

        for x in s:
            if x not in dic.keys():
                q.append(x)
            else:
                if not q:return False
                tmp = q.pop()
                if dic[x] != tmp:
                    return False
        if q: return False
        return True
