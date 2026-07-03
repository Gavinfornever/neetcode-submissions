class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        preNodes = {i:[] for i in range(n)}

        for n1, n2 in edges:
            preNodes[n1].append(n2)
            preNodes[n2].append(n1)

        visited = set()
        def dfs(node, par):
            if node in visited:
                return False

            visited.add(node)
            for nei in preNodes[node]:
                if nei == par: # 特别处理父子节点，不算是环
                    continue
                if not dfs(nei, node):
                    return False

            return True
        
        # for i in range(n):
        #     if not dfs(i, ):
        #         return False
        
        return dfs(0, -1) and len(visited) == n
