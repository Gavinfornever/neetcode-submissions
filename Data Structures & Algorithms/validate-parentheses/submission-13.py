class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        lefts = ['(','[','{']
        rights = [')',']','}']
        d = {
            '(':')',
            '{':'}',
            '[':']'
        }
        for c in s:
            if c in lefts:
                stack.append(c)
            else:
                if len(stack):
                    tmp = stack.pop()
                    if d[tmp]!=c:
                        return False
                else:return False
        if len(stack):return False
        return True