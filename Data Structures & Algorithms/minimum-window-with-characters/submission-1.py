import pickle
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dt = {}
        mn = float("inf")
        res = ""
        for c in t:
            dt[c] = dt.get(c, 0) + 1
        print(dt)
        l, r = 0,0

        dr = pickle.loads(pickle.dumps(dt))
        while l<len(s):
            # print(l)
            while l<len(s) and (s[l] not in dt):
                l+=1
                r=l
                dr = pickle.loads(pickle.dumps(dt))
            
            if l>=len(s):break

            if s[r] in dr:
                dr[s[r]]-=1
                if dr[s[r]]==0:
                    del dr[s[r]]

            if len(dr)==0:
                # print("ends")
                if (r-l+1) < mn:
                    res = s[l:r+1]
                    mn = r-l+1

                l+=1
                r=l
                dr = pickle.loads(pickle.dumps(dt))
                continue
            r+=1
            if r==len(s):
                l+=1
                r=l
                dr = pickle.loads(pickle.dumps(dt))

        return res
                