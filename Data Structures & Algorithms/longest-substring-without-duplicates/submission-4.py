class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:return 0
        if len(s)==1:return 1
        mx = 1
        l, r = 0, 1
        st = set()
        st.add(s[l])
        while r<len(s):
            if s[r] not in st:
                st.add(s[r])
                r+=1
                mx = max(mx, r-l)
            else:
                l+=1
                r=l+1
                st = set()
                st.add(s[l])
        
        return mx