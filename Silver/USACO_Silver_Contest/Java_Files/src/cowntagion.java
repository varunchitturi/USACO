import java.util.*;
public class cowntagion {
    static double total = 0;
    static HashMap<Integer, node> nodeMap = new HashMap<>();
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        for(int i = 0; i < n-1; i++){
            int first, second; first = in.nextInt(); second = in.nextInt();

            if(nodeMap.containsKey(first)){
                if(!nodeMap.containsKey(second)){
                    node a = new node(0);
                    nodeMap.put(second,a);
                   nodeMap.get(first).child.add(a);
                   a.child.add(nodeMap.get(first));
                }
                else{
                    nodeMap.get(first).child.add(nodeMap.get(second));
                    nodeMap.get(second).child.add(nodeMap.get(first));
                }
            }
            else{
                if(nodeMap.containsKey(second)){
                    node a = new node(0);
                    nodeMap.put(first,a);
                    nodeMap.get(second).child.add(a);
                    a.child.add(nodeMap.get(second));
                }
                else {
                    node a = new node(0);
                    nodeMap.put(first,a);
                    node b = new node(0);
                    nodeMap.put(second, b);
                    a.child.add(b);
                    b.child.add(a);
                }
            }
        }
        nodeMap.get(1).cowNum++;
        dfs(nodeMap.get(1));
        System.out.println((int)total);
    }
    static void dfs(node n){
        if(!n.visited){
            n.visited = true;
            int count = 0;
            for(int i = 0; i < n.child.size();i++){
                if(!n.child.get(i).visited){
                    count++;
                }
            }
            while(n.cowNum <= count){
                n.cowNum *= 2;
                total++;
            }
            n.cowNum -= count;
            for(int i = 0; i < n.child.size();i++){
                if(!n.child.get(i).visited){
                    n.child.get(i).cowNum++;
                    total++;
                    dfs(n.child.get(i));
                }
            }
        }
    }
    static class node{
        boolean visited = false;
        double cowNum;
        ArrayList<node> child = new ArrayList<>();
        public node(int n){
            this.cowNum = n;
        }
    }
}
