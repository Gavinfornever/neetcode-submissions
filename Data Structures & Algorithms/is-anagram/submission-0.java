
class Solution {
    Map<String,Integer> getMap(String s){
        Map<String,Integer> map = new HashMap<>();
        for(int x=0; x<s.length(); x++){
            String m=String.valueOf(s.charAt(x));
            if (!map.containsKey(m)){
                map.put(m,1);
            }else{
                map.put(m, map.get(m)+1);
            }
        }
        return map;
    }

    public boolean isAnagram(String s, String t) {
        Map<String,Integer> mapS = getMap(s);
        Map<String,Integer> mapT = getMap(t);
        if(mapS.equals(mapT)){
            return true;
        }else{
            return false;
        }

    }
}
