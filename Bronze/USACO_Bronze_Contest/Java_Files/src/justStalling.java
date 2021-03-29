import java.util.Arrays;
import java.util.Scanner;

public class justStalling {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int [] cows = new int[N];
        int [] stalls = new int[N];
        for(int i = 0; i < N; i++){
            cows[i] = in.nextInt();
        }
        for(int i = 0; i < N; i++){
            stalls[i]=in.nextInt();
        }
        long ans = 1;
        Arrays.sort(cows);
        Arrays.sort(stalls);
        int used = 0;
        for(int i = N-1; i >= 0; i--){
            int count = 0;
            for(int j = 0; j < N; j++){
                if(stalls[j] >= cows[i]){
                    count++;
                }
            }

            ans*=( count-used);
            used++;
        }
        System.out.println(ans);
    }
}
