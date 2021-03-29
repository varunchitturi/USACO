import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class HeatWave {
    static Comparator<qElement> nodeCompare = new Comparator<qElement>() {
        @Override
        public int compare(qElement o1, qElement o2) {
            return Integer.compare(o1.currCost, o2.currCost);
        }
    };
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int numTowns = in.nextInt();
        int numRoads = in.nextInt();
        int start = in.nextInt(); int end = in.nextInt();
        node [] nodeMap = new node[numTowns+1];
        for(int i = 0; i < numRoads; i++){
            int a = in.nextInt(); int b = in.nextInt(); int cost = in.nextInt();
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
        node source = nodeMap[start];
        PriorityQueue<qElement> q = new PriorityQueue<>(nodeCompare);
        if(start == end){
            System.out.println(0);
        }
        else{
            for(int i = 0; i < source.child.size();i++){
                q.add(new qElement(source.child.get(i).node,source.child.get(i).cost));
            }
            while(!q.isEmpty()){
                qElement curr = q.poll();
                if(!curr.node.isVisited){
                    curr.node.isVisited = true;
                    if(curr.node.val == end){
                        System.out.println(curr.currCost);
                        break;
                    }
                    for(int i = 0; i < curr.node.child.size();i++){
                        q.add(new qElement(curr.node.child.get(i).node, curr.currCost + curr.node.child.get(i).cost));
                    }
                }
            }
        }
    }
    static class qElement{
        node node;
        int currCost;

        public qElement(node node, int currCost) {
            this.node = node;
            this.currCost = currCost;
        }
    }
    static class node{
        boolean isVisited = false;
        int val;
        ArrayList<nodeChild> child = new ArrayList<>();

        public node(int val) {
            this.val = val;
        }
    }
    static class nodeChild{
        node node;
        int cost;

        public nodeChild(HeatWave.node node, int cost) {
            this.node = node;
            this.cost = cost;
        }
    }
}
