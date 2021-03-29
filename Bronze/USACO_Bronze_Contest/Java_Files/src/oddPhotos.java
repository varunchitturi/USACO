import java.util.Scanner;

public class oddPhotos {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int numOdds = 0, numEvens = 0;
        for(int i = 0; i < N; i++){
            int next = in.nextInt();
            if(next % 2 == 0){
                numEvens++;
            }
            else{
                numOdds++;
            }
        }




        int numSetsEven = numEvens;
        int numSetsOdd = numOdds;
        int minusN = 0;
        int max = 0;
        while(true){
            if(minusN *2 > numOdds){
                break;
            }
            numSetsEven = numEvens + minusN;
            numSetsOdd = numOdds - minusN*2;
            for(int i = 0; i <= numSetsEven; i++){
                if(i == numSetsOdd+1 || i== numSetsOdd){
                    if(i + numSetsOdd > max){
                        max = i + numSetsOdd;
                    }
                }
            }
            minusN++;
        }

        System.out.println(max);
    }
}
