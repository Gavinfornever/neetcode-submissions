class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = set()
        cur =""

        choices = {
            '2':['a','b', 'c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
        }
        def dfs(i):
            nonlocal cur
            if i==len(digits):
                if cur:
                    res.add(cur)
                return
            
            for x in choices[digits[i]]:
                cur+=x
                dfs(i+1)
                cur=cur[:-1]

        dfs(0)
        return list(res)