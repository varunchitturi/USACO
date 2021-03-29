import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class DijkstrasShortestPath {
    static Comparator<qElement> nodeCompare = new Comparator<qElement>() {
        @Override
        public int compare(qElement o1, qElement o2) {
            return Integer.compare(o1.currCost, o2.currCost);
        }
    };
    public static void main(String[] args) {
        boolean [] check = new boolean[2501];
        for(int i = 0; i < 2501;i++){
            check[i] = false;
        }
        Scanner in = new Scanner(System.in);
        int V,E,S;
        V = in.nextInt(); E = in.nextInt(); S = in.nextInt();
        node [] nodeMap = new node[V+1];
        for(int i = 0; i < E; i++){
            int v1, v2,dist;
            v1 = in.nextInt(); v2 = in.nextInt(); dist = in.nextInt();
            if(nodeMap[v1] == null){
                if(nodeMap[v2] == null){
                    nodeMap[v1] = new node(v1);
                    nodeMap[v2] = new node(v2);
                    nodeMap[v1].childInitial.add(new childNode(nodeMap[v2],dist));
                    nodeMap[v2].childInitial.add(new childNode(nodeMap[v1],dist));
                }
                else{
                    nodeMap[v1] = new node(v1);
                    nodeMap[v1].childInitial.add(new childNode(nodeMap[v2],dist));
                    nodeMap[v2].childInitial.add(new childNode(nodeMap[v1],dist));
                }
            }
            else{
                if(nodeMap[v2] == null){
                    nodeMap[v2] = new node(v2);
                    nodeMap[v1].childInitial.add(new childNode(nodeMap[v2],dist));
                    nodeMap[v2].childInitial.add(new childNode(nodeMap[v1],dist));
                }
                else{
                    nodeMap[v1].childInitial.add(new childNode(nodeMap[v2],dist));
                    nodeMap[v2].childInitial.add(new childNode(nodeMap[v1],dist));
                }
            }
        }
        int [] ans = new int [2501];
        for(int i = 0; i < 2501; i++){
            ans[i] = -1;
        }
        node head = nodeMap[S];
        PriorityQueue<qElement> q = new PriorityQueue<>(nodeCompare);

        for(int j = 0; j < head.childInitial.size(); j++){
            q.add(new qElement(head.childInitial.get(j).distance,head.childInitial.get(j)));
        }
        while(!q.isEmpty()){
            qElement curr = q.poll();
           if(!check[curr.node.n.val]){
               ans[curr.node.n.val] = curr.currCost;
                check[curr.node.n.val] = true;
                for(int j  = 0; j < curr.node.n.childInitial.size(); j++){
                    q.add(new qElement(curr.node.n.childInitial.get(j).distance + curr.currCost, curr.node.n.childInitial.get(j)));
                }
            }
        }
        ans[S] = 0;
        for(int i = 1; i <= V; i++){
            System.out.println(ans[i]);
        }

    }
    static class qElement{
        int currCost;
        childNode node;

        public qElement(int currCost, childNode node) {
            this.currCost = currCost;
            this.node = node;
        }
    }
    static class node{
        boolean isVisited = false;
        int val;
        ArrayList<childNode> childInitial = new ArrayList<>();
        public node(int val) {
            this.val = val;
        }
    }

    static void reset(node [] map){
        for(int i = 1; i < map.length; i++){
            map[i].isVisited = false;
        }
    }


    static class childNode{
        node n;
        int distance;

        public childNode(node n, int distance) {
            this.n = n;
            this.distance = distance;
        }
    }
}
