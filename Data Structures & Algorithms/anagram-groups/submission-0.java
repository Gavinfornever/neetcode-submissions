class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List> map = new HashMap<>();
        for(int i=0;i<strs.length;i++){
            // 排序
            char[] arr = strs[i].toCharArray();
            Arrays.sort(arr);
            String x = new String(arr);
            if (map.containsKey(x)){
                List list = map.get(x);
                list.add(new String(strs[i].toCharArray()));
                map.put(x, list);
            }else{
                List list = new ArrayList();
                list.add(new String(strs[i].toCharArray()));
                map.put(x, list);
            }
        }
        List<List<String>> res = new ArrayList<>();
        for (Map.Entry<String, List> entry: map.entrySet()){
            res.add(entry.getValue());
        }
        return res;
    }
}
