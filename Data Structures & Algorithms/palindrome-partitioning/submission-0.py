class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = set()
        cur = []
        def isPalindrome(s):
            length = len(s)
            for i in range(length//2):
                if s[i]!=s[length-i-1]:
                    return False
            return True

        def dfs(start):
            if start==len(s):
                res.add(tuple(cur))
                return
            
            for end in range(start, len(s)):
                if isPalindrome(s[start:end+1]):
                    cur.append(s[start:end+1])
                    dfs(end+1)
                    cur.pop()
                

            
        dfs(0)
        return [list(x) for x in res]


