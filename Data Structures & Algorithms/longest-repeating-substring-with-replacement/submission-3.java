class Solution {
    public int characterReplacement(String s, int k) {
        int maxLength = 0;
        for(int i=0;i<s.length();i++){
            Map<Character, Integer> map = new HashMap<>();
            map.put(s.charAt(i), 1);
            for(int j=i+1;j<s.length();j++){
                map.put(s.charAt(j), map.getOrDefault(s.charAt(j), 0)+1);
                int mostChar = Collections.max(map.values());
                if( (j-i+1 - mostChar)>k ){
                    break;
                }
                maxLength = Math.max(maxLength, j-i+1);
            }
        }
        return maxLength;
    }
}
