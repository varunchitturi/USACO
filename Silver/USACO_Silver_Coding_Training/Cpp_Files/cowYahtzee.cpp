#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;
int numDice, numSides, numExpressions;
struct comb{
    int num, side;
};
struct combinations{
    int counts[9] = {0};
    int comb [20] = {0};
};
vector<comb> all [20];
int num = 0;

bool check(combinations currentComb){
    bool c;
    for(int i = 0; i < numExpressions;i++){
        c = true;
        for(int j = 0; j < all[i].size();j++){
            if(currentComb.counts[all[i][j].side] < all[i][j].num){
                c = false;
                break;
            }
        }
        if(c){
            return true;
        }
    }
    return false;
}
void makeCombinations(int i, combinations currentComb){
    if(i == numDice){
        //allComb.push_back(currentComb);;
        if(check(currentComb)){
            num++;
        }
        return;
    }
    for(int j =1; j <= numSides;j++){
        combinations next;
        for(int k = 0; k < 20;k++){
            next.comb[k] = currentComb.comb[k];
        }
        for(int k = 0; k< 9;k++){
            next.counts[k] = currentComb.counts[k];
        }
        next.comb[i] = j; next.counts[j]++;
        makeCombinations(i+1,next);
    }
}
int main() {
    cin >> numDice >> numSides >> numExpressions;
    for(int i = 0; i < numExpressions;i++){
        string s; cin >> s;
        vector<string> split;
        string current = "";
        for(int j = 0; j < s.size();j++) {
            if(s[j] == 'x' || s[j] == '+'){
                split.push_back(current);
                current = "";
            }
            else{
                current += s[j];
            }
        }
        split.push_back(current);
        vector<comb> final;
        for(int j = 0; j < split.size();j+=2){
            comb toAdd; toAdd.num = stoi(split[j]); toAdd.side = stoi(split[j+1]);
            final.push_back(toAdd);
        }
        all[i] = final;
    }

    combinations start;
    makeCombinations(0,start);
    cout << num;
    return 0;
}