#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <unordered_set>
#include <queue>
#include <unordered_map>

using namespace std;


int matrix [5][5];
long c = 0;
int R,C,K;
void dfs(int i , int j, int count){
    if(i >= 0 && i < R && j >= 0 && j < C && count < K && matrix[i][j] != -1){
        if(i == 0 && j == C -1){
            c++;
            return;
        }
        matrix[i][j] = -1;
        dfs(i+1,j,count+1);
        dfs(i-1,j,count+1);
        dfs(i,j+1,count+1);
        dfs(i,j-1,count+1);
        matrix[i][j] = 0;
    }
}
int main() {
    cin >> R >> C >> K;
    for(int i = 0; i < R; i++){
        string in; cin >> in;
        for(int j = 0; j < C; j++){
            if(in[j] == '.'){
                matrix[i][j] = 0;
            }
            else{
                matrix[i][j] = -1;
            }
        }
    }
    dfs(R-1,0,0);
    cout << c;
    return 0;
}