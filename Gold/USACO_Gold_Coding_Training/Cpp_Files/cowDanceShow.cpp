//
// Created by Varun Chitturi on 10/6/20.
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


int solve(const vector<int>& q, int k){
    priority_queue<int, vector<int>, greater<int>> ans;
    int i;
    for(i = 0; i < k;i++){
        ans.push(q[i]);
    }

    int time = 0;
    while(!ans.empty()){
        time += ans.top();
        //int curr = ans.top();
        ans.pop();
        if(ans.size() != 0){
            int curr2 = ans.top();
            curr2 -= time; ans.pop(); ans.push(curr2);
        }
        if(i < q.size()){
            ans.push(q[i]+time);
            i++;
        }
    }
    return time;
}
int main() {
    int n, maxTime;
    vector<int> times;
    cin >> n >> maxTime;
    for(int i = 0; i < n; i++){
        int in; cin >> in;
        times.push_back(in);
    }

    for(int k = 2; k <= n; k++){
        if(solve(times,k) <= maxTime){
            cout << k;
            exit(1);

        }
    }

    return 0;
}
