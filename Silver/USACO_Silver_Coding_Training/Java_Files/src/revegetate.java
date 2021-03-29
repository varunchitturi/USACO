package src;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.*;
public class revegetate {
    static Node [] nodeMap;
    static int count2;
    static int [] sim;
    static String finalAns;
    static HashMap<String, String> instruct;
    static Scanner in;
    static Instruct [] instructions;
    public static void main(String[] args) throws FileNotFoundException {
        //in = new Scanner(System.in);
        File f = new File("revegetate.in");
        in = new Scanner(f);
        instruct = new HashMap<>();
        int N = in.nextInt();
        int M = in.nextInt();
        nodeMap = new Node[N+1];
        instructions = new Instruct[M];
        for(int i = 0; i < M; i++){
            String a = in.next();
            int b = in.nextInt();
            int c = in.nextInt();
            String n = b + " " + c;
            String n2 = c + " " + b;
            if(instruct.containsKey(n) && !instruct.get(n).equals(a)){
                finalAns = "0";
                in.close();
                  PrintWriter w = new PrintWriter("revegetate.out");
                 w.write(finalAns);
                 w.close();
                //System.out.println(finalAns);
                System.exit(0);
            }
            instructions[i] = new Instruct(a,b,c);
            instruct.put(n,a);
            instruct.put(n2,a);
            if(nodeMap[b] == null){
                if(nodeMap[c] == null){
                    nodeMap[b] = new Node(b);
                    nodeMap[c] = new Node(c);
                    nodeMap[b].child.add(nodeMap[c]);
                    nodeMap[c].child.add(nodeMap[b]);
                }
                else{
                    nodeMap[b] = new Node(b);
                    nodeMap[b].child.add(nodeMap[c]);
                    nodeMap[c].child.add(nodeMap[b]);
                }
            }
            else{
                if(nodeMap[c] == null){
                    nodeMap[c] = new Node(c);
                    nodeMap[b].child.add(nodeMap[c]);
                    nodeMap[c].child.add(nodeMap[b]);
                }
                else{
                    nodeMap[b].child.add(nodeMap[c]);
                    nodeMap[c].child.add(nodeMap[b]);
                }
            }
        }
        int total = N;
        int count = 0;
        for(int i = 0; i < N; i++){
            int curr = i+1;
            count2 = 0;

            if(nodeMap[curr] != null && !nodeMap[curr].isVisited){
                dfs(nodeMap[curr]);
                count++;
            }
            total -= count2;
        }
        StringBuilder b = new StringBuilder();
        b.append("1");
        for(int i = 0; i< total+count;i++){
            b.append("0");
        }
        finalAns = b.toString();
        sim = new int[N];
        Arrays.fill(sim,-1);
        for(int i = 0; i < N; i++){
            if(nodeMap[i+1] != null && nodeMap[i+1].isVisited){
                dfsRev(nodeMap[i+1]);
            }
        }
        for(int i = 0; i < M; i++){
            if(instructions[i].s.equals("S")){
                int n1 = instructions[i].a;
                int n2 = instructions[i].b;
                if(sim[n1-1] != sim[n2-1]){
                    finalAns = "0";
                    break;
                }
            }
            else{
                int n1 = instructions[i].a;
                int n2 = instructions[i].b;
                if(sim[n1-1] == sim[n2-1]){
                    finalAns = "0";
                    break;
                }
            }
        }
        in.close();
      PrintWriter w = new PrintWriter("revegetate.out");
       w.write(finalAns);
        w.close();
        //System.out.println(finalAns);

    }
    static class Instruct{
        String s;
        int a;
        int b;

        public Instruct(String s, int a, int b) {
            this.s = s;
            this.a = a;
            this.b = b;
        }
    }
    static void dfs(Node curr){
        curr.isVisited = true;
        count2++;
        for(int i = 0; i < curr.child.size(); i++){
            if(!curr.child.get(i).isVisited){
                dfs(curr.child.get(i));
            }
        }
    }
    static void dfsRev(Node curr) throws FileNotFoundException {
        curr.isVisited = false;
        for(int j = 0; j < curr.child.size();j++){
            if(curr.child.get(j).isVisited){
                int n1 = curr.val;
                int n2 = curr.child.get(j).val;
                String currS = curr.val + " " +  curr.child.get(j).val;
                if(instruct.get(currS).equals("S")){
                    if(sim[n1-1] == -1 || sim[n2-1] == -1){
                            if(sim[n1-1] == sim[n2-1]){
                                sim[n1-1] = 1;
                                sim[n2-1] = 1;
                            }
                            else if(sim[n1-1] == -1){
                                sim[n1-1] = sim[n2-1];
                            }
                            else{
                                sim[n2-1] = sim[n1-1];
                            }
                    }
                    else if(sim[n1-1] != sim[n2-1]){
                        finalAns = "0";
                        in.close();
                      PrintWriter w = new PrintWriter("revegetate.out");
                        w.write(finalAns);
                        w.close();
                        //System.out.println(finalAns);
                        System.exit(0);
                    }
                }
                else{
                    if(sim[n1-1] == -1 || sim[n2-1] == -1){
                        if(sim[n1-1] == sim[n2-1]){
                            sim[n1-1] = 1;
                            sim[n2-1] = 0;
                        }
                        else if(sim[n1-1] == -1){
                            if(sim[n2-1] == 1){
                                sim[n1-1] = 0;
                            }
                            else{
                                sim[n1-1] = 1;
                            }
                        }
                        else{
                            if(sim[n1-1] == 1){
                                sim[n2-1] = 0;
                            }
                            else{
                                sim[n2-1] = 1;
                            }
                        }
                    }
                    else if(sim[n1-1] == sim[n2-1]){
                        finalAns = "0";
                        in.close();
                        PrintWriter w = new PrintWriter("revegetate.out");
                        w.write(finalAns);
                        w.close();
                        //System.out.println(finalAns);
                        System.exit(0);
                    }
                }
                dfsRev(curr.child.get(j));
            }
        }
    }
    static class Node{
        int val;
        boolean isVisited = false;
        ArrayList<Node> child = new ArrayList<>();
        public Node(int val) {
            this.val = val;
        }
    }
}
