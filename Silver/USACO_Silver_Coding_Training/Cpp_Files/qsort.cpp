#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;


static int numNumbers;
static vector<int> allNums;

void p(vector<int> a){
    for(int i = 0; i < numNumbers;i++){
        cout << a[i] << " ";
    }
    cout << "\n";
}
void swap(int * a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
int part(int low, int high){

    int l = low-1;
    int h = high;
    int done = allNums[high];
    while(true){
        while(allNums[++l] < done ){

        }
        while(done < allNums[--h]){

        }
        if(h==1){
            break;
        }
        if (l >= h){

            break;
        }
        swap(allNums[l], allNums[h]);


    }
    swap(allNums[l], allNums[high]);



    p(allNums);
    return l;

}

void quicksort(int start, int stop){
    if(stop <= start){return;}
    int pivot = part(start, stop);
    quicksort(start, pivot-1);

    quicksort(pivot+1, stop);





}
int main(){
    cin >> numNumbers;
    int a;
    for(int i = 0; i< numNumbers;i++){
        cin >> a;
        allNums.push_back(a);
    }
    quicksort(0, numNumbers-1);
    //p(allNums);




    return 0;

}




