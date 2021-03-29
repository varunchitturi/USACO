import java.util.*;

public class moooo {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        ArrayList<cow> cows = new ArrayList<>();
        ArrayList<cow> cowSorted = new ArrayList<>();
        ArrayList<cow> cowPopper = new ArrayList<>();
        int n = in.nextInt();
        for(int i = 0; i < n; i++) {
            int h, v;
            h = in.nextInt();
            v = in.nextInt();
            cows.add(new cow(h, v, 0, i));
            cowSorted.add(new cow(h, v, 0, i));
            cowPopper.add(new cow(h, v, 0, i));
        }
        Collections.sort(cowSorted, new Comparator<cow>(){
            public int compare(cow s1, cow s2) {
                if(s1.h == s2.h){
                    return 0;
                }
                return s1.h > s2.h ? 1 : -1;
            }
        });
        for(int i = 0 ; i < n; i++){
            int index = cowSorted.get(i).i;
            int pIndex = search(cowPopper, index);
            if(pIndex + 1 < cowPopper.size()){
                cows.get(cowPopper.get(pIndex+1).i).num += cowPopper.get(pIndex).v;
            }
            if(pIndex - 1 >= 0){
                cows.get(cowPopper.get(pIndex-1).i).num += cowPopper.get(pIndex).v;
            }
            cowPopper.remove(pIndex);
        }
        int max = 0;
        for(int i = 0; i < n; i++){
            if(cows.get(i).num > max){
                max = cows.get(i).num;
            }
        }
        System.out.println(max);
    }

    static class cow{
        int h,v,num,i;
        public cow(int h, int v, int num, int i) {
            this.h = h;
            this.v = v;
            this.num = num;
            this.i = i;
        }
    }
    static int search(ArrayList<cow> arr, int x)
    {
        int l = 0, r = arr.size() - 1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (arr.get(m).i == x)
                return m;
            if (arr.get(m).i < x)
                l = m + 1;
            else
                r = m - 1;
        }
        return -1;
    }

}
