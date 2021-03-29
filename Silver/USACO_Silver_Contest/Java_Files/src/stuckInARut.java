import java.util.*;

public class stuckInARut {
    static HashMap<String, Integer> ate = new HashMap<>();
    static int [] ans;
    static int stopped = 0;
    static int maxX, maxY;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        ans = new int[n];
        move [] m = new move[n];
        maxX = 0; maxY = 0;
        for(int i = 0; i < n; i++){
            String b = in.next();
            int x = in.nextInt(); int y = in.nextInt();
            if(x > maxX){
                maxX = x;
            }
            if(y > maxY){
                maxY = y;
            }
            if(b.equals("E")){
                m[i] = new move(1,x,y);
            }
            else{
                m[i] = new move(0,x,y);
            }

        }
        while(true){
           increment(m);
            for(int i = 0; i < m.length;i++){
                if(ate.containsKey(createString(m[i]))){
                    m[i].direction = -1;
                    ans[ate.get(createString(m[i]))]++;
                    stopped++;
                }
                else{
                    ate.put(createString(m[i]),i);
                }
                if(m[i].x > maxX){
                    maxX = m[i].x;
                }
                if(m[i].y > maxY){
                    maxY = m[i].y;
                }
                if(m[i].x == maxX && m[i].y == maxY){
                    m[i].direction = -1;
                    stopped++;
                }
            }
            if(stopped == n){
                break;
            }
        }
        for(int i = 0; i < ans.length;i++){
            System.out.println(ans[i]);
        }
    }

    static void increment(move [] a){
        for(int i = 0; i < a.length; i++){
            if(a[i].direction == 1){
                a[i].x++;
            }
            else if(a[i].direction == 0){
                a[i].y++;
            }
        }
    }
    static String createString(move a){
        return Integer.toString(a.x) + " " + Integer.toString(a.y);
    }
    static class move{
        int direction; // 1 right 0 is up
        int x,y;

        public move(int direction, int x, int y) {
            this.direction = direction;
            this.x = x;
            this.y = y;
        }
    }
}
