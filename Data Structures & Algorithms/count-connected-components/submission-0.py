class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        dic = {i:[] for i in range(n)}

        for n1, n2 in edges:
            dic[n1].append(n2)
            dic[n2].append(n1)
        
        num = 0
        visited = set()
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            for x in dic[node]:
                dfs(x)
            return 1
        
        for i in range(n):
            num+=dfs(i)
        
        return num




