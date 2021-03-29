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
int matrix[1000][1000];
int R,C;
int c= 0;
void dfs(int a, int b){
    stack<pair<int,int>> s;
    s.push(make_pair(a,b));
    while(!s.empty()) {
        int i = s.top().first; int j = s.top().second;
        matrix[i][j] = 0;
        s.pop();
        if (i > 0 && matrix[i - 1][j] == 1) {
            s.emplace(i - 1, j);
        }
        if (i < R - 1 && matrix[i + 1][j] == 1) {
            s.emplace(i + 1, j);
        }
        if (j > 0 && matrix[i][j - 1] == 1) {
            s.emplace(i, j - 1);
        }
        if (j < C - 1 && matrix[i][j + 1] == 1) {
            s.emplace(i, j + 1);
        }
        if (i > 0 && j > 0 && matrix[i - 1][j - 1] == 1) {
            s.emplace(i - 1, j - 1);
        }
        if (i > 0 && j < C - 1 && matrix[i - 1][j + 1] == 1) {
            s.emplace(i - 1, j + 1);
        }
        if (i < R - 1 && j > 0 && matrix[i + 1][j - 1] == 1) {
            s.emplace(i + 1, j - 1);
        }
        if (i < R - 1 && j < C - 1 && matrix[i + 1][j + 1] == 1) {
            s.emplace(i + 1, j + 1);
        }
    }
}
int main() {
    cin >> R >> C;
    int in;
    for(int i = 0; i < R; i++){
        for(int j = 0; j < C; j++){
            cin >> in;
            if(in == 0){
                matrix[i][j] = 0;
            }
            else{
                matrix[i][j] = 1;
            }
        }
    }
    for(int i = 0; i < R; i++){
        for(int j = 0; j < C;j++){
            if(matrix[i][j] == 1){
                c++;
                dfs(i,j);
            }
        }
    }
    cout << c;
    return 0;
}