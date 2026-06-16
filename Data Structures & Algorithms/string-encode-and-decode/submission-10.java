class Solution {

    public String encode(List<String> strs) {
        if(strs.isEmpty())return "";
        StringBuffer sb = new StringBuffer();
        for(String str: strs){
            sb.append(str + "好");
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        if (str.isEmpty())return new ArrayList<String>();
        List<String> res = new ArrayList<String>();
        String[] strs =  str.split("好");
        if(strs.length==0){
            res.add("");
            return res;
        }
        res = Arrays.asList(strs);
        return res;
    }
}
