class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l=1, r=numbers.length;
        int[] res= new int[2];
        while(l<r){
            if((numbers[l-1]+numbers[r-1])==target){
                res[0] = l;
                res[1] = r;
                return res;
            }else if((numbers[l-1]+numbers[r-1])<target){
                l+=1;
            }else{
                r-=1;
            }
        }
        return res;
    }
}
