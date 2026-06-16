class Solution {
    public boolean isValid(String s) {
        // // if s.length is odd, return false
        // if(s.length()%2!=0)return false;
        // Stack<Character> st = new Stack<>();
        // // corresponding table of brackets
        Map<Character, Character> map = new HashMap<>();
        map.put('{','}');
        // map.put('}','{');
        map.put('[',']');
        // map.put(']','[');
        map.put('(',')');
        // map.put(')','(');
        // // put half of all brackets in the stack
        // for(int i=0;i<=(s.length()/2-1);i++){
        //     st.push(s.charAt(i));
        // }
        // for(int i=(s.length()/2);i<s.length();i++){
        //     if( map.get(s.charAt(i)) != st.pop())return false;
        // }
        // return true;

        Stack<Character> stack= new Stack<>();
        // for every char, put in stack if not correspond to the former one
        for(int i=0;i<s.length();i++){
            if(stack.empty()){
                // if when empty and add right bracket, false
                if(!map.containsKey(s.charAt(i))){
                    return false;
                }
                // else just put in
                stack.push(s.charAt(i));
                continue;
            }
            // when not empty, most cases
            // we want to check cur char 
            // if left just put in and quit
            if(map.containsKey(s.charAt(i))){
                stack.push(s.charAt(i));
                continue;
            }
            // if right, check if can form a matching
            if( map.get(stack.peek()) == s.charAt(i)){
                stack.pop();
            }else{
                return false;
            }
        }
        if(stack.empty()){
            return true;
        }else{
            return false;
        }
    }
}
