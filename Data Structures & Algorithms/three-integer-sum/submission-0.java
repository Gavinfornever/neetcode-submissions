class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        Map<Integer, Integer> map = new HashMap<>();
        Set<List<Integer>> set = new HashSet<>();
        for(int i=0;i<nums.length;i++){
            map.put(nums[i], i);//把本值放进去
        }
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                int tmpSum = nums[i]+nums[j];
                if(map.containsKey(-tmpSum)){
                    List<Integer> tmpArr = new ArrayList<>(3);
                    int val = map.get(-tmpSum);
                    if (val==i || val==j){
                        continue;
                    }
                    tmpArr.add( Math.max(Math.max(nums[i], nums[j]), -tmpSum) );
                    tmpArr.add( Math.min(Math.min(nums[i], nums[j]), -tmpSum) );
                    tmpArr.add( nums[i]+nums[j]-tmpSum-tmpArr.get(0) -tmpArr.get(1) );
                    set.add(tmpArr);
                }
            }
        }
        System.out.println(set);
        return new ArrayList<>(set);
    }
}
