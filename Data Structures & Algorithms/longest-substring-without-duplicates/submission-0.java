class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l=0, r=0;
        int maxLen = 0;
        Set<String> set = new HashSet();
        while(r<s.length()){
            if(!set.add(s.substring(r,r+1))){
                l+=1;
                r=l;
                set = new HashSet();
                continue;
            }
            maxLen = Math.max(maxLen, set.size());
            r+=1;
        }
        return maxLen;
    }
}
