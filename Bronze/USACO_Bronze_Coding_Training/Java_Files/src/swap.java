
import java.util.*;
import java.io.*;
public class swap {
    public static void main(String [] args) throws Exception {
        File in = new File("swap.in");
        Scanner input = new Scanner(in);
        int numCows = input.nextInt();
        int times = input.nextInt();
        int a1 = input.nextInt();
        int a2 = input.nextInt();
        int b1 = input.nextInt();
        int b2 = input.nextInt();

        int [] cows = new int[numCows];
        ArrayList<int []> ord = new ArrayList<>();
        HashSet<String> done = new HashSet<>();
        for(int i = 0; i < numCows; i++){
            cows[i] = i+1;
        }
        ord.add(Arrays.copyOf(cows,cows.length));
        done.add(Arrays.toString(cows));
        int count = 0;
        while(true){
            if(count == times){
                try {
                    BufferedWriter out = new BufferedWriter(new FileWriter("swap.out"));
                    for(int i = 0; i < numCows; i++){
                        out.write(Integer.toString(cows[i]));
                        out.write("\n");
                    }
                    out.close();
                    System.out.println("works");
                }
                catch (Exception e){
                    System.out.println("does not work");
                }
                break;
            }
            reverse(a1,a2,b1,b2,cows);
            if(done.contains(Arrays.toString(cows))){
                try {
                    BufferedWriter out = new BufferedWriter(new FileWriter("swap.out"));
                    for(int i = 0; i < numCows; i++){
                        out.write(Integer.toString((ord.get(times % ord.size()))[i]));
                        out.write("\n");
                    }
                    out.close();
                    System.out.println("works");
                }
                catch (Exception e){
                    System.out.println("does not work");
                }
                break;
            }
            else{
                ord.add(Arrays.copyOf(cows,cows.length));
                done.add(Arrays.toString(cows));
            }
            count++;
        }


    }
    public static void reverse(int a1, int a2, int b1, int b2, int [] ab){
        for(int i = 0; i < ((a2-a1)/2)+1; i++){
            int temp = ab[a1-1+i];
            ab[a1-1+i] = ab[a2-1-i];
            ab[a2-1-i] = temp;
        }
        for(int i = 0; i < ((b2-b1)/2)+1; i++){
            int temp = ab[b1-1+i];
            ab[b1-1+i] = ab[b2-1-i];
            ab[b2-1-i] = temp;
        }
    }
}
