package src;

import java.io.File;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class paintingTheBarn {
    static Point [] points;
    static int K;
    static int ans = 0;
    public static void main(String[] args) {
        Comparator<Point> p = new Comparator<Point>() {
            @Override
            public int compare(Point o1, Point o2) {
                if(o1.x1 < o2.x1){
                    return -1;
                }
                else if(o1.x1 == o2.x1){
                    return 0;
                }
                return 1;
            }
        };
        Scanner in = new Scanner(System.in);
        // File f = new File("paintbarn.in");
        // Scanner in = new Scanner(f);

        int N = in.nextInt();
        K = in.nextInt();

        points = new Point[N];

        for(int i = 0; i < N; i++){
            points[i] = new Point(in.nextInt(), in.nextInt(), in.nextInt(), in.nextInt());
        }
        Arrays.sort(points,p);

        System.out.println(ans);
    }

    static class Point{
        int x1, y1, x2, y2;
        boolean done = false;
        public Point(int x1, int y1, int x2, int y2) {
            this.x1 = x1;
            this.y1 = y1;
            this.x2 = x2;
            this.y2 = y2;
        }
    }

}
