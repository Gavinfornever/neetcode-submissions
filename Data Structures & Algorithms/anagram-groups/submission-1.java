class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        //先对每个字符串进行统计，利用第一套hashmap
        List<Map> list1 = new ArrayList<>();
        for (int i=0;i<strs.length;i++){
            Map<Character, Integer> map1 = new HashMap<>();
            char[] str = strs[i].toCharArray();
            for (int j=0;j<str.length;j++){
                if (!map1.containsKey(str[j])){
                    map1.put(str[j], 1);
                }else{
                    map1.put(str[j], map1.get(str[j])+1);
                }
            }
            list1.add(map1);
        }
        //对归类好的map数组 通过比较得到新的分组，利用第二套hashmap，映射关系和对应下标
        Map<Map, List> map2 = new HashMap<>();
        for (int i=0;i<list1.size();i++){
            if (!map2.containsKey(list1.get(i))){
                List tmpList = new ArrayList<String>();
                tmpList.add(strs[i]);
                map2.put(list1.get(i), tmpList);
            }else{
                List tmpList = map2.get(list1.get(i));
                tmpList.add(strs[i]);
                map2.put(list1.get(i), tmpList);
            }
        }
        //遍历返回结果
        List<List<String>> res = new ArrayList<>();
        for (Map.Entry<Map, List> entry: map2.entrySet()){
            res.add(entry.getValue());
        }
        return res;
    }
}
