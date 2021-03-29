import java.util.*;
public class hayBales{
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        int numHaybales = input.nextInt();
        int hay[][] = new int[numHaybales][2];
        //size then position

        for (int i = 0; i < numHaybales; i++) {

            hay[i][0] = input.nextInt();
            hay[i][1] = input.nextInt();

        }

        Arrays.sort(hay,  new Comparator<int[]>() {

            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[1] - o2[1];
            }

        });
        int left = 0;
        int right = 0;
        int sumOfArea = 0;
        int pow = 0;
        for (int i = 0;i<numHaybales-1;i++){
            left = i;
            right = i+1;
            while (left >= 0 && right < numHaybales){
                pow = hay[right][1] - hay[left][1];
                if (pow <= hay[right][0] && pow <= hay[left][0]){
                    //        System.out.println();
                    sumOfArea += (hay[i+1][1] - hay[i][1]);
                    break;
                }
                if (pow > hay[right][0]){
                    right++;
                }
                if (pow > hay[left][0]){
                    left--;
                }

            }


        }

        System.out.println(sumOfArea);

    }
}
