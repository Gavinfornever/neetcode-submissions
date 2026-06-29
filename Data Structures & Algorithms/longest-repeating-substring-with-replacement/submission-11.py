class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k>=len(s):return len(s)
        if len(s)==1:return 1
        l, r = 0, 1
        mx = 0

        mxf = 0

        dic = {}
        dic[s[l]] = 1
        while r<len(s):
            if s[r] in dic:
                dic[s[r]]+=1
            else:
                dic[s[r]]=1
            
            # print(l, r)

            # for i in range(l,r+1):
            #     # print(i)
            #     if s[i] not in dic:
            #         dic[s[i]]=1
            #     else:
            #         dic[s[i]]+=1

            # print(dic)

            mxn = max(dic, key=dic.get)
            mxc = dic[mxn]

            # print("mxc+k:", mxc+k)
            # print("r-l+1:", r-l+1)
            if mxc+k >=(r-l+1):
                mx = max(mx, r-l+1)
                r+=1
            else:
                # mx = max(mx, r-l+1)
                dic[s[l]]-=1
                l+=1
                dic = {}
                dic[s[l]]=1
                r=l+1

            # print("mx:", mx)

        return mx

        # x y y z y x , 2
        # a b a b a b a b c c c a 
        # 1
