//
// Created by Varun Chitturi on 1/24/21.
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
int places [100000];
vector<vector<int>> allPos;
vector<unordered_set<int>> id;
vector<int> ans;
int N,K;

void dfs(int pos, unordered_set<int>* currID, unordered_set<int> *encountered){
    if(encountered->find(pos) != encountered->end()){
        for (const auto& elem: *encountered) {
           ans[elem] = currID->size();
        }
        return;
    }
    encountered->insert(pos);
    if(ans[pos] != 0){
        for (const auto& elem: *encountered) {
            ans[elem] = ans[pos];
        }
        return;
    }
    for (const auto& elem: id[pos]) {
        currID->insert(elem);
    }
    dfs(allPos[pos][allPos[pos].size()-1],currID,encountered);
}

int main() {
    cin >> N >> K;
    for(int i = 0; i < N; i++){
        ans.push_back(0);
        places[i] = i;
        allPos.emplace_back();
        id.emplace_back();
        allPos[i].push_back(i);
        id[i].insert(i);
    }
    for(int i = 0; i < K; i++){
        int a,b; cin >> a >> b;
        allPos[places[a-1]].push_back(b-1);
        id[places[a-1]].insert(b-1);
        id[places[b-1]].insert(a-1);
        allPos[places[b-1]].push_back(a-1);
        int temp = places[a-1];
        places[a-1] = places[b-1];
        places[b-1] = temp;
    }
    for(int i = 0; i < N; i++){
        if(ans[i] == 0){
            unordered_set<int> a;
            unordered_set<int> b;
            dfs(i, &a, &b);
        }

    }
    for(int i = 0; i < N; i++){
        cout << ans[i] << "\n";
    }
    return 0;
}
