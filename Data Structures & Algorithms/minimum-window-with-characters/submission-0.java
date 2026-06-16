class Solution {
    public boolean ifEmpty(Map<Character, Integer> map){
        for(Integer v:map.values()){
            if(v>0){
                return false;
            }
        }
        return true;
    }
    public Map<Character, Integer> getCountMap(String t){
        Map<Character, Integer> map = new HashMap<>();
        for(int m=0;m<t.length();m++){
            map.put(t.charAt(m), map.getOrDefault(t.charAt(m),0)+1);
        }
        return map;
    }
    public String minWindow(String s, String t) {
        Map<Character, Integer> map = new HashMap<>();
        int minLength = 100;
        String res = "";
        for(int l=0;l<s.length();l++){
            // get all characters' count table
            map = getCountMap(t);
            // move left to first letter, if not move
            if(!map.containsKey(s.charAt(l))){ // arrived at the first letter
                continue;
            }
            // move right till the map is empty
            for(int r=l;r<s.length();r++){
                // del r's character from map
                if(map.containsKey(s.charAt(r))){
                    map.put(s.charAt(r), map.getOrDefault(s.charAt(r), 0)-1);
                }
                // if map becomes empty, get the intermediate result
                if(ifEmpty(map)){
                    if((r-l+1)<minLength){
                        minLength = r-l+1;
                        res = s.substring(l, r+1);
                    }
                    break;
                }
            }

        }
        return res;
        // for(int i=0;i<s.length();i++){
        //     //
        //     for(int m=0;m<t.length();m++){
        //         map.put(t.charAt(m), map.getOrDefault(t.charAt(m),0)+1)
        //     }
        //     //
        //     if(map.getOrDefault(s.charAt(i), 0)<=0){
        //         continue;
        //     }
        //     for(int j=i;j<s.length();j++){
        //         if(map.getOrDefault(s.charAt(j), 0)==0){
        //             continue;
        //         }
        //         map.put(s.charAt(j), map.getOrDefault(t.charAt(i),0)-1);
        //     }
        //     for(Integer n:map.values()){
        //         if(n>0){//means there are still some characters left, unsuccessful.
        //             break;
        //         }
        //     }
            
        // }

    }
}
