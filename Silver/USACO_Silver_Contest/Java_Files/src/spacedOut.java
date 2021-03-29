import javax.swing.*;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class spacedOut {
    static int bestScore = 0;
    static int N;
    static int [][] visited;
    static int [][] pMatrix;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        N = in.nextInt();
        pMatrix = new int[N][N];
        for(int i = 0 ;i < N; i++){
            for(int j = 0; j < N; j++){
                pMatrix[i][j] = in.nextInt();
            }
        }
        visited = new int [N][N];
        comb(0,0,0);
        System.out.println(bestScore);

    }

   static void comb(int score, int i, int j){
        if(score > bestScore){
            bestScore = score;
        }
        int toAdd = 0;
        if(i== N-1 && j== N-1){
            return;
        }
        if(i < N-1 && j < N-2){
            
            toAdd = 0;
            if(visited[i][j] == 0){
                toAdd += pMatrix[i][j];
            }
            if(visited[i+1][j] == 0){
                toAdd += pMatrix[i+1][j];
           }
            visited[i][j]++; visited[i+1][j]++;
           if(check(i,j) && check(i+1,j)){
                comb(score+toAdd,i,j+1);
            }
            visited[i][j]--; visited[i+1][j]--;

            toAdd = 0;
           if(visited[i][j] == 0){
                toAdd += pMatrix[i][j];
           }
           if(visited[i][j+1] == 0){
                toAdd += pMatrix[i][j+1];
           }
            visited[i][j]++; visited[i][j+1]++;
           if(check(i,j) && check(i,j+1)){
                comb(score+toAdd,i,j+1);
           }
            visited[i][j]--; visited[i][j+1]--;

            toAdd = 0;
           if(visited[i][j+1] == 0){
                toAdd += pMatrix[i][j+1];
           }
           if(visited[i+1][j+1] == 0){
                toAdd += pMatrix[i+1][j+1];
           }
            visited[i][j+1]++; visited[i+1][j+1]++;
           if(check(i,j+1) && check(i+1,j+1)){
                comb(score+toAdd,i,j+1);
           }
            visited[i][j+1]--; visited[i+1][j+1]--;

            toAdd = 0;
           if(visited[i+1][j] == 0){
                toAdd += pMatrix[i+1][j];
           }
            if(visited[i+1][j+1] == 0){
                toAdd += pMatrix[i+1][j+1];
            }
            visited[i+1][j]++; visited[i+1][j+1]++;
           if(check(i+1,j) && check(i+1,j+1)){
                comb(score+toAdd,i,j+1);
           }
            visited[i+1][j]--; visited[i+1][j+1]--;

            toAdd = 0;
           if(visited[i][j+1] == 0){
                toAdd += pMatrix[i][j+1];
           }
           if(visited[i+1][j] == 0){
                toAdd += pMatrix[i+1][j];
           }
            visited[i][j+1]++; visited[i+1][j]++;
           if(check(i,j+1) && check(i+1,j)){
                comb(score+toAdd,i,j+1);
           }
            visited[i][j+1]--; visited[i+1][j]--;

            toAdd = 0;
           if(visited[i][j] == 0){
                toAdd += pMatrix[i][j];
           }
           if(visited[i+1][j+1] == 0){
                toAdd += pMatrix[i+1][j+1];
            }
            visited[i][j]++; visited[i+1][j+1]++;
            if(check(i,j) && check(i+1,j+1)){
                comb(score+toAdd,i,j+1);
            }
            visited[i][j]--; visited[i+1][j+1]--;
        }
        else if (i < N-1){

            toAdd = 0;
           if(visited[i][j] == 0){
                toAdd += pMatrix[i][j];
            }
            if(visited[i+1][j] == 0){
                toAdd += pMatrix[i+1][j];
            }
            visited[i][j]++; visited[i+1][j]++;
            if(check(i,j) && check(i+1,j)){
                comb(score+toAdd,i+1,0);
           }
           visited[i][j]--; visited[i+1][j]--;

            toAdd = 0;
            if(visited[i][j] == 0){
                toAdd += pMatrix[i][j];
            }
            if(visited[i][j+1] == 0){
                toAdd += pMatrix[i][j+1];
            }
           visited[i][j]++; visited[i][j+1]++;
            if(check(i,j) && check(i,j+1)){
                comb(score+toAdd,i+1,0);
            }
           visited[i][j]--; visited[i][j+1]--;

            toAdd = 0;
            if(visited[i][j+1] == 0){
                toAdd += pMatrix[i][j+1];
           }
           if(visited[i+1][j+1] == 0){
                toAdd += pMatrix[i+1][j+1];
           }
           visited[i][j+1]++; visited[i+1][j+1]++;
            if(check(i,j+1) && check(i+1,j+1)){
                comb(score+toAdd,i+1,0);
           }
           visited[i][j+1]--; visited[i+1][j+1]--;

            toAdd = 0;
            if(visited[i+1][j] == 0){
                toAdd += pMatrix[i+1][j];
            }
           if(visited[i+1][j+1] == 0){
                toAdd += pMatrix[i+1][j+1];
           }
           visited[i+1][j]++; visited[i+1][j+1]++;
            if(check(i+1,j) && check(i+1,j+1)){
                comb(score+toAdd,i+1,0);
           }
           visited[i+1][j]--; visited[i+1][j+1]--;

            toAdd = 0;
            if(visited[i][j+1] == 0){
                toAdd += pMatrix[i][j+1];
           }
            if(visited[i+1][j] == 0){
                toAdd += pMatrix[i+1][j];
           }
            visited[i][j+1]++; visited[i+1][j]++;
            if(check(i,j+1) && check(i+1,j)){
                comb(score+toAdd,i+1,0);
           }
           visited[i][j+1]--; visited[i+1][j]--;

            toAdd = 0;
            if(visited[i][j] == 0){
                toAdd += pMatrix[i][j];
            }
            if(visited[i+1][j+1] == 0){
                toAdd += pMatrix[i+1][j+1];
            }
            visited[i][j]++; visited[i+1][j+1]++;
            if(check(i,j) && check(i+1,j+1)){
                comb(score+toAdd,i+1,0);
           }
            visited[i][j]--; visited[i+1][j+1]--;
        }
   }
   static boolean check(int i, int j){
        
        int TL = 0, TR = 0, BL = 0, BR = 0;
        if(i+1 < N){
            if(visited[i+1][j]!=0){
                BL++; BR++;
            }

            if(j+1 < N && visited[i+1][j+1]!=0){
                BR++;
            }
            if(j-1 >= 0 && visited[i+1][j-1]!=0){
                BL++;
            }
        }
        if(j+1 < N && visited[i][j+1] !=0){
            BR++; TR++;
        }
        if(i-1 >= 0){
            if(visited[i-1][j]!=0){
                TR++;TL++;
            }
            if(j+1 < N && visited[i-1][j+1] !=0){
                TR++;
            }
            if(j-1 >= 0 && visited[i-1][j-1] !=0){
                TL++;
            }
        }
        if(j-1 >= 0 && visited[i][j-1]!=0){
            BL++;
            TL++;
        }
        if(TR >= 2 || TL >= 2 || BL >= 2 || BR >= 2){
            return false;
        }
        return true;
   }
}
