class MinStack {
    public List<Integer> list=null;
    public MinStack() {
        list = new ArrayList<Integer>();
    }
    
    public void push(int val) {
        list.add(val);
    }
    
    public void pop() {
        list.remove(list.size()-1);
    }
    
    public int top() {
        return list.get(list.size()-1);
    }
    
    public int getMin() {
        return Collections.min(list);
    }
}
