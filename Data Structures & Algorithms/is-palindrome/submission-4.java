class Solution {
    private boolean isLetters(char c){
        if (('a'<=c&&c<='z')||('A'<=c&&c<='Z')){
            return true;
        }
        return false;
    }

    private boolean isNumber(char c){
        if ('0'<=c&&c<='9'){
            return true;
        }
        return false;
    }

    private boolean isEqual(char x, char y){
        if(x==y)return true;
        if(isLetters(x)&&isLetters(y)){
            if(x<y&&((x+'a'-'A')==y))return true;
            if(y<x&&((y+'a'-'A')==x))return true;
        }
        return false;
    }

    public boolean isPalindrome(String s) {
        int i=0, j=s.length()-1;
        while(i<j){
            char left = s.charAt(i);
            char right = s.charAt(j);
            //是否在范围内
            if(!isLetters(left)&&!isNumber(left)){
                i++;
                continue;
            }else if(!isLetters(right)&&!isNumber(right)){
                j--;
                continue;
            }
            //判断是否相等
            if (!isEqual(left, right)){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}

