import java.util.Scanner;

public class udderedNotHerd {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String alpha = in.next();
        String heard = in.next();
        int ans = 0;
        int curr = 0;
        while(curr < heard.length()){
            ans++;
            for(int i = 0; i < alpha.length(); i++){
                if(alpha.charAt(i) == heard.charAt(curr)){
                    curr++;
                    if(curr == heard.length()){
                        break;
                    }
                }
            }
        }
        System.out.println(ans);
    }
}
