class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l,r = n, n
        
        res = set()
        cur = ""
        def dfs(k, cl, cr):
            nonlocal cur
            if k==2*n and cl==n and cr==n:
                res.add(cur)
                return
            if cl<n:
                cur += "("
                dfs(k+1, cl+1, cr)
                cur = cur[:-1]
            if cr<n and cr<cl:
                cur += ")"
                dfs(k+1, cl, cr+1)
                cur = cur[:-1]
        dfs(0, 0, 0)
        return list(res)