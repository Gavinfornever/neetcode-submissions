class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = set()
        cur = []
        # candidates.sort()

        def dfs(i,cur,total):
            if total==target:
                res.add(tuple(cur))
                return 
            if total>target or i>=len(candidates):
                return
            
            #if want num i
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])
            #if not
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0,[],0)

        # dedup
        # seen = set()
        # tmp = []
        # for item in res:
        #     tuple_item = tuple(item)
        #     if tuple_item not in seen:
        #         seen.add(tuple_item)
        #         tmp.append(item)

        return [list(comb) for comb in res]