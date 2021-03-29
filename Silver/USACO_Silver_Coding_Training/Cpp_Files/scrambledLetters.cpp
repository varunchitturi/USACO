//
// Created by Varun Chitturi on 5/28/20.
//


#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#define MAXN 500000
using namespace std;


string allCows[MAXN];

struct name{
    string str;
    int index;
    bool reversed;
    bool operator<(name const& n) const {
        if (str == n.str) {
            return (reversed == false) && n.reversed == true;
        }
        return str < n.str; }
};

name allInputs[100000];
int worst[MAXN];
int best[MAXN];


int main(){
    int numNames;
    cin >> numNames;
    for(int i = 0; i< numNames;i++){
        cin >> allCows[i];
    }
    for (int i = 0; i < numNames; i++) {
        sort(allCows[i].begin(), allCows[i].end());
        allInputs[2*i].str = allCows[i]; allInputs[2*i].index = i; allInputs[2*i].reversed = false;
        allInputs[2*i+1].str = allCows[i]; reverse(allInputs[2*i+1].str.begin(), allInputs[2*i+1].str.end()); allInputs[2*i+1].index = i;
        allInputs[2*i+1].reversed = true;
    }
    sort(allInputs, allInputs + (2*numNames));
    int numReversed = 0;
    for (int i = 0; i < 2*numNames; i++) {
        if (allInputs[i].reversed) { numReversed++;
        } else {
            int index = allInputs[i].index; worst[index] = numReversed + 1;
        } }
    int countForewards = 0;
    for (int i = 2*numNames-1; i >= 0; i--) {
        if (!allInputs[i].reversed) { countForewards++;
        } else {
            int index = allInputs[i].index; best[index] = numNames - countForewards;
        } }

    for(int i = 0;i < numNames;i++){
        cout << worst[i] <<" "<<best[i] << "\n";
    }
}
