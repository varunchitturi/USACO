import java.util.*;

public class stuckInARut {
    static cow [] cows;
    static cow [] cowInitial;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        cows = new cow[n];
        cowInitial = new cow[n];
        for(int i = 0 ; i< n;i++){
            String direction = in.next(); int x = in.nextInt(); int y = in.nextInt();
            cows[i] = new cow(direction,x,y);
            cowInitial[i] = new cow(direction,x,y);
        }
        String [] ans = new String[n];
        Arrays.fill(ans, "-1");

        int stoppedCount = 0;
        while(stoppedCount < n){
            int toIncrease = Integer.MAX_VALUE;
            for(int i= 0; i < cows.length;i++){
                if(!cows[i].isStopped){
                    int num = checkInfinite(cows[i]);
                    if(num == -1){
                        if(!ans[i].equals("Infinity")){
                            ans[i] = "Infinity";
                            stoppedCount++;
                        }
                    }
                    else{
                        if(toIncrease > checkInfinite(cows[i])){
                            toIncrease = checkInfinite(cows[i]);
                        }
                    }
                }
            }
            if(stoppedCount == n){
                break;
            }
            for(int i = 0; i < cows.length;i++){
                if(cows[i].direction.equals("E") && !cows[i].isStopped){
                    cows[i].x += toIncrease;
                }
                else if(!cows[i].isStopped){
                    cows[i].y += toIncrease;
                }
                cows[i].eaten += toIncrease;
            }
            for(int i = 0; i < cows.length;i++){
                for(int j =0; j < cows.length; j++){
                    if(!cows[i].isStopped && cows[i].direction.equals("E") && cows[j].direction.equals("N" ) ){
                        if(cows[i].x == cows[j].x && cows[j].y > cows[i].y && cowInitial[j].y <= cows[i].y ){
                            ans[i] = Integer.toString(cows[i].eaten);
                            cows[i].isStopped = true;
                            stoppedCount++;
                            break;
                        }
                    }
                    else if(!cows[i].isStopped && cows[i].direction.equals("N" ) && cows[j].direction.equals("E")){
                        if(cows[i].y == cows[j].y && cows[j].x > cows[i].x && cowInitial[j].x <= cows[i].x){
                            ans[i] = Integer.toString(cows[i].eaten);
                            cows[i].isStopped = true;
                            stoppedCount++;
                            break;
                        }
                    }
                }
            }
        }
        for(int i =0; i < ans.length;i++){
            System.out.println(ans[i]);

        }
    }
    static int checkInfinite(cow a){
        int bestDist = Integer.MAX_VALUE;
        if(a.direction.equals("E")){
            for(int i = 0; i < cows.length;i++){
                if(!cows[i].isStopped){
                        if(cows[i].direction.equals("N") && cows[i].x >= a.x  && cows[i].x-a.x > a.y-cows[i].y && cowInitial[i].y <= a.y){
                            if(bestDist >cows[i].x-a.x){
                                bestDist = cows[i].x-a.x;
                            }
                        }
                }
                else{
                    if(cows[i].direction.equals("N") && (cows[i].y >= a.y && cowInitial[i].y <= a.y && cows[i].x > a.x) ){
                        if(bestDist >cows[i].x-a.x){
                            bestDist = cows[i].x-a.x;
                        }
                    }

                }
            }
        }
        else{
            for(int i = 0; i < cows.length;i++){
                if(!cows[i].isStopped){
                        if(cows[i].direction.equals("E") && cows[i].y >= a.y && cows[i].y - a.y > a.x - cows[i].x && cowInitial[i].x <= a.x){
                            if(bestDist >cows[i].y-a.y){
                                bestDist = cows[i].y-a.y;
                            }
                        }
                }
                else{
                    if(cows[i].direction.equals("E") && (cows[i].x >= a.x && cowInitial[i].x <= a.x && cows[i].y > a.y)){
                        if(bestDist >cows[i].y-a.y){
                            bestDist = cows[i].y-a.y;
                        }
                    }
                }

            }
        }
        if(bestDist == Integer.MAX_VALUE){
            return -1;
        }
        else{
            return bestDist;
        }
    }
    static class cow{
        String direction;
        int x,y;
        boolean isStopped = false;
        int eaten = 0;
        public cow(String direction, int x, int y) {
            this.direction = direction;
            this.x = x;
            this.y = y;
        }
    }
}
