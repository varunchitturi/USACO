//
// Created by Varun Chitturi on 10/15/20.
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

int main() {
    int numCows, numGroups;
    cin >> numCows >> numGroups;
    vector<unordered_set<int>> groups;
    for(int i = 0; i < numGroups; i++){
        int count; cin >> count;
        groups.emplace_back();
        for(int j = 0; j < count; j++){
            int in; cin >> in;
            groups[i].insert(in);
        }
    }
    int ans = 1;
    for(int i = 0; i < groups.size(); i++){
        if(groups[i].find(1) != groups[i].end()){
            groups[i].erase(1);
        }
    }
    unordered_set<int> invited;
    invited.insert(1);
    while(true){
        vector<int> toRemove;
        for(int i = 0; i < groups.size();i++){
            if(groups[i].size() == 1){
                toRemove.push_back(*groups[i].begin());
                if(invited.find(*groups[i].begin()) == invited.end()){
                    ans += 1;
                    invited.insert(*groups[i].begin());
                }
            }
        }
        if(toRemove.empty()){
            break;
        }
        else{
            for(int j = 0; j < toRemove.size();j++){
               for(int k = 0; k < groups.size();k++){
                   if(groups[k].find(toRemove[j]) != groups[k].end()){
                       groups[k].erase(toRemove[j]);
                   }
               }
            }
        }
    }
    cout << ans;
    return 0;
}
