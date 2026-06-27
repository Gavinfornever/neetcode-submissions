from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if length%2!=0:return False

        dic = {
            '[':']',
            ']':'[',
            '(':')',
            ')':'(',
            '{':'}',
            '}':'{',
        }
        q = deque()
        for i in range(length//2):
            q.append(s[i])
        
        for i in range(length//2, length-1):
            tmp = q.pop()
            if dic[tmp] !=s[i]:
                return False
        
        return True