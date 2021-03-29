//
// Created by Varun Chitturi on 9/26/20.
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

int m,n;

void toggle(int i, int j, vector<vector<bool>> * a){
    (*a)[i][j] == 1 ? (*a)[i][j] = 0 : (*a)[i][j] = 1;
    if(i > 0){
        (*a)[i-1][j] == 1 ? (*a)[i-1][j] = 0 : (*a)[i-1][j] = 1;
    }
    if(i < m-1){
        (*a)[i+1][j] == 1 ? (*a)[i+1][j] = 0 : (*a)[i+1][j] = 1;
    }
    if(j > 0){
        (*a)[i][j-1] == 1 ? (*a)[i][j-1] = 0 : (*a)[i][j-1] = 1;
    }
    if(j < n-1){
        (*a)[i][j+1] == 1 ? (*a)[i][j+1] = 0 : (*a)[i][j+1] = 1;
    }
}
void print(const vector<vector<bool>> grid){
    for(int i=  0; i < m; i++){
        for(int j = 0; j < n ;j++){
            cout << grid[i][j] << " ";
        }
        cout << "\n";
    }
}
bool check(const vector<vector<bool>> grid){
    for(int i = 0 ; i < m; i++){
        for(int j = 0; j < n; j++){
            if(grid[i][j] != false){
                return false;
            }
        }
    }
    return true;
}
void solve(vector<vector<bool>> grid, vector<vector<bool>> flipped){
    for(int i = 1; i < m;i++){
        for(int j = 0; j < n; j++){
            if(grid[i-1][j] == true){
                toggle(i,j,&grid);
                flipped[i][j] = true;
            }
        }
    }
    if(check(grid)){
        print(flipped);
        exit(0);
    }
}

void makeFirst(int start, vector<vector<bool>> grid, vector<vector<bool>> flipped){
    solve(grid,flipped);
    for(int j = start; j < n; j++){
        vector<vector<bool>> next = grid; vector<vector<bool>> newflip = flipped;
        newflip[0][j] = true; toggle(0,j,&next);
        makeFirst(j+1,next,newflip);
    }
}
int main() {
    cin >> m >> n;
    vector<vector<bool>> grid;
    vector<vector<bool>> flip;
    for(int i = 0; i < m; i ++){
        grid.emplace_back();
        flip.emplace_back();
        for(int j = 0; j < n; j++) {
            int in; cin >> in;
            grid[i].push_back((bool)in);
            flip[i].push_back(false);
        }
    }
    makeFirst(0,grid,flip);

    cout << "IMPOSSIBLE";
}