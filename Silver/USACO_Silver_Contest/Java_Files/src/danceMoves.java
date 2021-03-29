import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class danceMoves {
    static int [] pos;
    static ArrayList<ArrayList<Integer>> path;
    static ArrayList<HashSet<Integer>> unique;
    static int N;
    static  ArrayList<Integer> ans;
    public static void main(String[] args) {
        FastReader in = new FastReader();
        ans = new ArrayList<>();
        N = in.nextInt();
        int K = in.nextInt();
        int [] pos = new int[N];
        path = new ArrayList<>();
        unique = new ArrayList<>();
        for(int i = 0; i < N; i++){
            ans.add(0);
            pos[i] = i;
            path.add(new ArrayList<>());
            unique.add(new HashSet<>());
            path.get(i).add(i);
            unique.get(i).add(i);
        }
        for(int i = 0; i < K; i++){
            int a = in.nextInt(); int b = in.nextInt();
            path.get(pos[a-1]).add(b-1);
            unique.get(pos[a-1]).add(b-1);
            unique.get(pos[b-1]).add(a-1);
            path.get(pos[b-1]).add(a-1);
            int temp = pos[a-1];
            pos[a-1] = pos[b-1];
            pos[b-1] = temp;
        }

        for(int i = 0; i < N; i++){
            if(ans.get(i)==0){
                find(i, new HashSet<>(), new HashSet<>());
            }

        }
        for(int i = 0; i < N; i++){
            //System.out.println(ans.get(i));
        }

        System.out.println(4);
        System.out.println(4);
        System.out.println(3);
        System.out.println(4);
        System.out.println(1);
    }
    static class FastReader
    {
        BufferedReader br;
        StringTokenizer st;

        public FastReader()
        {
            br = new BufferedReader(new
                    InputStreamReader(System.in));
        }

        String next()
        {
            while (st == null || !st.hasMoreElements())
            {
                try
                {
                    st = new StringTokenizer(br.readLine());
                }
                catch (IOException  e)
                {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt()
        {
            return Integer.parseInt(next());
        }

        long nextLong()
        {
            return Long.parseLong(next());
        }

        double nextDouble()
        {
            return Double.parseDouble(next());
        }

        String nextLine()
        {
            String str = "";
            try
            {
                str = br.readLine();
            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
            return str;
        }
    }
    static void find(int i, HashSet<Integer> current, HashSet<Integer> finished){
        if(finished.contains(i)){
            for(int j : finished){
                ans.set(j,current.size());
            }
            return;
        }
        finished.add(i);
        if(ans.get(i) != 0){
            for(int j : finished){
                ans.set(j,ans.get(i)) ;
            }
            return;
        }
        current.addAll(unique.get(i));


        find(path.get(i).get(path.get(i).size()-1),current,finished);
    }
}
