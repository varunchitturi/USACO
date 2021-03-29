
#include <iostream>
using namespace std;
int main(){
    int numCows;
    cin >> numCows;
    int speeds[numCows];
    int a;
    for(int i = 0 ; i< numCows;i++){
        cin >> a >> speeds[i];
    }
    int numGroups = 1;
    for(int i = numCows-1 ;i > 0;i--){
        if(speeds[i] >= speeds[i-1]){
            numGroups++;
        }
        else{
            speeds[i-1] = speeds[i];
        }
    }
    cout << numGroups;
}
