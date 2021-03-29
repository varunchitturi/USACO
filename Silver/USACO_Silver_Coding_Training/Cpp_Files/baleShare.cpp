#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#define INT_MAX 2147483647
using namespace std;
static vector<int> bales;
static int numBales;
static int low = INT_MAX;
void makeCombinations(int i, int b1, int b2, int b3){
    if(i > numBales-1){
        if(b1 >= b2 && b1 >= b3){
            if(b1 < low){
                low = b1;
            }
        }
    }
    else{
        if(b1 + bales[i] < low){
            makeCombinations(i+1, b1+bales[i], b2, b3);}
        if(b2 + bales[i] < low){
            makeCombinations(i+1, b1, b2+bales[i], b3);}
        if(b3 + bales[i] < low){
            makeCombinations(i+1, b1, b2, b3+bales[i]);
        }

    }

}

int main(){
    cin >> numBales;
    int a;
    for(int i = 0; i < numBales;i++){
        cin >> a;
        bales.push_back(a);
    }
    makeCombinations(0, 0, 0, 0);
    /*
    int mina = INT_MAX;
    a = 0;
    for(int i = 0; i< possibleValuesb1.size();i++){
        if(mina > possibleValuesb1[i]){
            mina = possibleValuesb1[i];
            a = i;
        }
    }*/
    cout << low << "\n";
    /*
    cout << possibleValuesb1[a] << " " << possibleValuesb2[a] << " " << possibleValuesb3[a]<< "\n";
    for(int i = 0; i< possibleValuesb1.size();i++){
        cout << possibleValuesb1[i] << "\n";
    }
    */





    return 0;
}

