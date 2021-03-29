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
vector<int> arr;
struct comm{
    int a,b;
    comm(int a, int b) : a(a), b(b) {}
};
bool my_cmp(const comm& a, const comm& b)
{
    if(abs(a.a - a.b) != abs(b.a-b.b)){
        return abs(a.a - a.b) > abs(b.a-b.b);
    }
    return a.a < b.a;
}
void solve(comm curr){
    int m = min(arr[curr.a-1],arr[curr.b-1]);
    if (curr.a < curr.b){
        for(int i = curr.a; i < curr.b-1;i++){
            if(arr[i] >=m){
                arr[i] = m-1;
            }
        }
    }
    else{
        for(int i = curr.a-2; i >= curr.b;i--){
            if(arr[i] >= m){
                arr[i] = m-1;
            }
        }
    }
}
int main() {
    int n,I,h,r;
    cin >> n >> I >> h >> r;
    for(int i = 0; i < n; i++){
        arr.push_back(h);
    }
    vector<comm> comms;
    for(int i = 0; i < r; i++){
        int a,b; cin >> a >> b;
        comms.emplace_back(a,b);
    }
    sort(comms.begin(), comms.end(), my_cmp);
    for(int i = 0; i < r; i++){
        solve(comms[i]);
    }
    for(int i = 0; i < arr.size(); i++){
        cout << arr[i] << "\n";
    }

    return 0;
}
