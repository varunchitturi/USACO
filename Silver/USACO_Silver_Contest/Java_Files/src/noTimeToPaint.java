import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class noTimeToPaint {
    static Comparator<Integer> pq = new Comparator<Integer>() {
        @Override
        public int compare(Integer o1, Integer o2) {
            return Integer.compare(o1,o2)*-1;
        }
    };
    public static void main(String[] args) {
        FastReader in = new FastReader();
        int N = in.nextInt(), K = in.nextInt();
        String next = in.next();
        int [] prefixSumLeft = new int[N];
        int count = 0;
        int [] prefixSumRight = new int[N];
        PriorityQueue<Integer> lhs = new PriorityQueue<>(pq);
        PriorityQueue<Integer> rhs = new PriorityQueue<>(pq);
        for(int i = 0; i < N; i++){
            int lPaint = next.charAt(i);
            while(true){
                if(!lhs.isEmpty() && lhs.peek() > lPaint){
                    lhs.poll();
                }
                else{
                    break;
                }
            }
            if(lhs.isEmpty() || lPaint > lhs.peek()){
                count++;
                lhs.add(lPaint);
            }
            prefixSumLeft[i] = count;
        }

        count = 0;
        for(int i = N-1; i >= 0; i--){
            int currPaint = next.charAt(i);
            while(true){
                if(!rhs.isEmpty() && rhs.peek() > currPaint){
                    rhs.poll();
                }
                else{
                    break;
                }
            }
            if(rhs.isEmpty() || currPaint > rhs.peek()){
                count++;
                rhs.add(currPaint);
            }
            prefixSumRight[i] = count;
        }
        for(int i = 0; i < K; i++ ){
            int a = in.nextInt(), b = in.nextInt();
            int ans = 0;
            if(a != 1){
                ans += prefixSumLeft[a-2];
            }
            if(b!=N){
                ans += prefixSumRight[b];
            }
            System.out.println(ans);
        }
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
                catch (IOException e)
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
}
