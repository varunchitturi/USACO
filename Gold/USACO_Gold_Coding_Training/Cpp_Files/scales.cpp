//
// Created by Varun Chitturi on 9/21/20.
//

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <unordered_set>
#include <queue>
#include <unordered_map>
#include <stack>

using namespace std;
int numWeights, maxWeight;
vector<int> weights;
int m = 999999999;
void dfs(int currentNum, int amountLeft){
    if(m > amountLeft){
        m = amountLeft;
    }
    if(amountLeft>=0 && currentNum > 0)
    {
        if(weights[currentNum]+weights[currentNum-1] <= amountLeft){
            dfs(currentNum-1,amountLeft-weights[currentNum]);
        }
        else if(weights[currentNum] <= amountLeft && weights[currentNum] + weights[currentNum-1] > amountLeft ){
            dfs(currentNum-2,amountLeft-weights[currentNum]);
            dfs(currentNum-2,amountLeft-weights[currentNum-1]);
        }
        else{
            dfs(currentNum-1,amountLeft);
        }
    }
}
int main() {

    cin >> numWeights >> maxWeight;




    weights.push_back(0);
    for(int i = 0; i < numWeights; i++ ){
        int in; cin >> in;
            weights.push_back(in);
    }
    dfs(numWeights,maxWeight);
    cout << maxWeight-m;
    return 0;
}
