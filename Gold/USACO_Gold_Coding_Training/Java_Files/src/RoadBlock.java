import java.util.*;

public class RoadBlock {
    static Comparator<qElement> nodeCompare = new java.util.Comparator<qElement>() {
        @Override
        public int compare(qElement o1, qElement o2) {
            return Integer.compare(o1.currCost, o2.currCost);
        }
    };
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt(), M = in.nextInt();
        node [] nodeMap = new node[N+1];
        for(int i = 0; i < M; i++){
            int a = in.nextInt(), b = in.nextInt(), cost = in.nextInt();
            if(nodeMap[a] == null){
                if(nodeMap[b] == null){
                    nodeMap[a] = new node(a);
                    nodeMap[b] = new node(b);
                    nodeMap[a].child.add(new nodeChild(nodeMap[b],cost));
                    nodeMap[b].child.add(new nodeChild(nodeMap[a],cost));
                }
                else{
                    nodeMap[a] = new node(a);
                    nodeMap[a].child.add(new nodeChild(nodeMap[b],cost));
                    nodeMap[b].child.add(new nodeChild(nodeMap[a],cost));
                }
            }
            else{
                if(nodeMap[b] == null){
                    nodeMap[b] = new node(b);
                    nodeMap[a].child.add(new nodeChild(nodeMap[b],cost));
                    nodeMap[b].child.add(new nodeChild(nodeMap[a],cost));
                }
                else{
                    nodeMap[a].child.add(new nodeChild(nodeMap[b],cost));
                    nodeMap[b].child.add(new nodeChild(nodeMap[a],cost));
                }
            }
        }
        ArrayList<Integer> path = new ArrayList<>();
        PriorityQueue<qElement> q = new PriorityQueue<>(nodeCompare);
        node source = nodeMap[1];
        for(int i = 0; i < source.child.size();i++){
            qElement toAdd = new qElement(source.child.get(i) ,source.child.get(i).cost);
            toAdd.path.add(1); toAdd.path.add(source.child.get(i).node.val);
            q.add(toAdd);
        }

        int currentLength = -1;
        while(!q.isEmpty()){
            qElement curr = q.poll();
            if(!curr.node.node.isVisited){
                curr.node.node.isVisited = true;
                if(curr.node.node.val == N){
                    currentLength = curr.currCost;
                    path.addAll(curr.path);
                    break;
                }
                for(int i = 0; i < curr.node.node.child.size(); i++){
                    qElement toAdd = new qElement(curr.node.node.child.get(i),curr.currCost + curr.node.node.child.get(i).cost);
                    toAdd.path.addAll(curr.path);
                    toAdd.path.add(curr.node.node.child.get(i).node.val);
                    q.add(toAdd);
                }
            }
        }
        int worstCost = 0;

        for(int i=  0; i < path.size()-1;i++){
            for(int j= 1; j< N+1;j++){
                nodeMap[j].isVisited = false;
            }
            q.clear();
            for(int j = 0; j < source.child.size();j++){
                if(path.get(i) == source.val && path.get(i+1) == source.child.get(j).node.val){
                    qElement toAdd = new qElement(source.child.get(j) ,source.child.get(j).cost*2);
                    q.add(toAdd);
                }
               else{
                    qElement toAdd = new qElement(source.child.get(j) ,source.child.get(j).cost);
                    q.add(toAdd);
                }

            }
            while(!q.isEmpty()){
                qElement curr = q.poll();
                if(!curr.node.node.isVisited){
                    curr.node.node.isVisited = true;
                    if(curr.node.node.val == N){
                        if(curr.currCost > worstCost){
                            worstCost = curr.currCost;
                        }
                        //System.out.println(curr.currCost);
                        break;
                    }
                    for(int j = 0; j < curr.node.node.child.size(); j++){
                        if(curr.node.node.val == path.get(i) && curr.node.node.child.get(j).node.val == path.get(i+1)){
                            qElement toAdd = new qElement(curr.node.node.child.get(j),curr.currCost + curr.node.node.child.get(j).cost*2);
                            q.add(toAdd);

                        }
                        else{
                            qElement toAdd = new qElement(curr.node.node.child.get(j),curr.currCost + curr.node.node.child.get(j).cost);
                            q.add(toAdd);
                        }
                    }
                }
            }
        }
        System.out.println(worstCost-currentLength);
    }
    static class node{
        int val;
        ArrayList<nodeChild> child = new ArrayList<>();
        boolean isVisited = false;
        public node(int val) {
            this.val = val;
        }
    }
    static class nodeChild{
        int cost;
        node node;

        public nodeChild(node node, int cost) {
            this.cost = cost;
            this.node = node;
        }
    }
    static class qElement{
        nodeChild node;
        int currCost;
        ArrayList<Integer> path = new ArrayList<>();
        public qElement(nodeChild node, int currCost) {
            this.node = node;
            this.currCost = currCost;
        }
    }
}
