class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {}
        for p in prerequisites:
            if p[0] not in dic:
                dic[p[0]] = [p[1]]
            else:
                dic[p[0]].append(p[1])

        def dfs(c, p, pres):
            res = True
            if p in pres:
                return False
            pres.append(p)
            if p in dic:
                for i in range(len(dic[p])):
                    res = res and dfs(p, dic[p][i], pres)
            return res

        res = True
        for i in range(numCourses):
            if i in dic:
                res = res and dfs(i, dic[i][0],[])
        
        return res


