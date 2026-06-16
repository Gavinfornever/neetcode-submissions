class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        //先创建26长度的数组，统计每个字符串的字母
        //存入相应的hashmap中
        Map<String, List> map = new HashMap<>();
        for(String str: strs){
            int[] arr = new int[26];
            for (int i=0;i< str.length(); i++){
                arr[str.charAt(i)-'a']++;
            }
            //List arr2 = Arrays.asList(arr);
            StringBuffer sb = new StringBuffer();
            for (int x: arr){
                sb.append(x+"#");
            }
            String key = sb.toString();
            if(!map.containsKey(key)){
                List tmpList = new ArrayList<>();
                tmpList.add(str);
                map.put(key, tmpList);
            }else{
                List tmpList = map.get(key);
                tmpList.add(str);
                map.put(key, tmpList);
            }
        }
        List<List<String>> res = new ArrayList<>();
        for (List value: map.values()){
            res.add(value);
        }
        return res;
    }
}
