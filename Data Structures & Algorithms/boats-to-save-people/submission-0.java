class Solution {
    public int numRescueBoats(int[] people, int limit) {
        int l=0, r=people.length-1;
        Arrays.sort(people);
        int num = 0;
        while(l<=r){
            if((people[l]+people[r])<=limit){
                num+=1;
                l+=1;
                r-=1;
            }else if((people[l]+people[r])>limit){
                num+=1;
                r-=1;
            }
        }
        return num;
    }
}