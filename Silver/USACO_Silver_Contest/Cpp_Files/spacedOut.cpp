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
int best = 0;
int N;
int done[1000][1000];
int matrix[1000][1000];
bool isPossible(int a, int b){
    int ul = 0, ur = 0, dl = 0, br = 0;
    if(a+1 < N){
        if(done[a+1][b]!=0){
            dl+=1; br+=1;
        }

        if(b+1 < N && done[a+1][b+1]!=0){
            br+=1;
        }
        if(b-1 >= 0 && done[a+1][b-1]!=0){
            dl+=1;
        }
    }
    if(b+1 < N && done[a][b+1] !=0){
        br+=1; ur+=1;
    }
    if(a-1 >= 0){
        if(done[a-1][b]!=0){
            ur+=1;ul+=1;
        }
        if(b+1 < N && done[a-1][b+1] !=0){
            ur+=1;
        }
        if(b-1 >= 0 && done[a-1][b-1] !=0){
            ul+=1;
        }
    }
    if(b-1 >= 0 && done[a][b-1]!=0){
        dl+=1;
        ul+=1;
    }
    if(ur >= 2 || ul >= 2 || dl >= 2 || br >= 2){
        return false;
    }
    return true;
}
void dfs(int curr, int a, int b){
    if(curr > best){
        best = curr;
    }
    int toAdd = 0;
    if(a== N-1 && b== N-1){
        return;
    }
    if(a < N-1 && b < N-2){

        toAdd = 0;
        if(done[a][b] == 0){
            toAdd += matrix[a][b];
        }
        if(done[a+1][b] == 0){
            toAdd += matrix[a+1][b];
        }
        done[a][b]+=1; done[a+1][b]+=1;
        if(isPossible(a,b) && isPossible(a+1,b)){
            dfs(curr+toAdd,a,b+1);
        }
        done[a][b]-=1; done[a+1][b]-=1;

        toAdd = 0;
        if(done[a][b] == 0){
            toAdd += matrix[a][b];
        }
        if(done[a][b+1] == 0){
            toAdd += matrix[a][b+1];
        }
        done[a][b]+=1; done[a][b+1]+=1;
        if(isPossible(a,b) && isPossible(a,b+1)){
            dfs(curr+toAdd,a,b+1);
        }
        done[a][b]-=1; done[a][b+1]-=1;

        toAdd = 0;
        if(done[a][b+1] == 0){
            toAdd += matrix[a][b+1];
        }
        if(done[a+1][b+1] == 0){
            toAdd += matrix[a+1][b+1];
        }
        done[a][b+1]+=1; done[a+1][b+1]+=1;
        if(isPossible(a,b+1) && isPossible(a+1,b+1)){
            dfs(curr+toAdd,a,b+1);
        }
        done[a][b+1]-=1; done[a+1][b+1]-=1;

        toAdd = 0;
        if(done[a+1][b] == 0){
            toAdd += matrix[a+1][b];
        }
        if(done[a+1][b+1] == 0){
            toAdd += matrix[a+1][b+1];
        }
        done[a+1][b]+=1; done[a+1][b+1]+=1;
        if(isPossible(a+1,b) && isPossible(a+1,b+1)){
            dfs(curr+toAdd,a,b+1);
        }
        done[a+1][b]-=1; done[a+1][b+1]-=1;

        toAdd = 0;
        if(done[a][b+1] == 0){
            toAdd += matrix[a][b+1];
        }
        if(done[a+1][b] == 0){
            toAdd += matrix[a+1][b];
        }
        done[a][b+1]+=1; done[a+1][b]+=1;
        if(isPossible(a,b+1) && isPossible(a+1,b)){
            dfs(curr+toAdd,a,b+1);
        }
        done[a][b+1]-=1; done[a+1][b]-=1;

        toAdd = 0;
        if(done[a][b] == 0){
            toAdd += matrix[a][b];
        }
        if(done[a+1][b+1] == 0){
            toAdd += matrix[a+1][b+1];
        }
        done[a][b]+=1; done[a+1][b+1]+=1;
        if(isPossible(a,b) && isPossible(a+1,b+1)){
            dfs(curr+toAdd,a,b+1);
        }
        done[a][b]-=1; done[a+1][b+1]-=1;
    }
    else if (a < N-1){

        toAdd = 0;
        if(done[a][b] == 0){
            toAdd += matrix[a][b];
        }
        if(done[a+1][b] == 0){
            toAdd += matrix[a+1][b];
        }
        done[a][b]+=1; done[a+1][b]+=1;
        if(isPossible(a,b) && isPossible(a+1,b)){
            dfs(curr+toAdd,a+1,0);
        }
        done[a][b]-=1; done[a+1][b]-=1;

        toAdd = 0;
        if(done[a][b] == 0){
            toAdd += matrix[a][b];
        }
        if(done[a][b+1] == 0){
            toAdd += matrix[a][b+1];
        }
        done[a][b]+=1; done[a][b+1]+=1;
        if(isPossible(a,b) && isPossible(a,b+1)){
            dfs(curr+toAdd,a+1,0);
        }
        done[a][b]-=1; done[a][b+1]-=1;

        toAdd = 0;
        if(done[a][b+1] == 0){
            toAdd += matrix[a][b+1];
        }
        if(done[a+1][b+1] == 0){
            toAdd += matrix[a+1][b+1];
        }
        done[a][b+1]+=1; done[a+1][b+1]+=1;
        if(isPossible(a,b+1) && isPossible(a+1,b+1)){
            dfs(curr+toAdd,a+1,0);
        }
        done[a][b+1]-=1; done[a+1][b+1]-=1;

        toAdd = 0;
        if(done[a+1][b] == 0){
            toAdd += matrix[a+1][b];
        }
        if(done[a+1][b+1] == 0){
            toAdd += matrix[a+1][b+1];
        }
        done[a+1][b]+=1; done[a+1][b+1]+=1;
        if(isPossible(a+1,b) && isPossible(a+1,b+1)){
            dfs(curr+toAdd,a+1,0);
        }
        done[a+1][b]-=1; done[a+1][b+1]-=1;

        toAdd = 0;
        if(done[a][b+1] == 0){
            toAdd += matrix[a][b+1];
        }
        if(done[a+1][b] == 0){
            toAdd += matrix[a+1][b];
        }
        done[a][b+1]+=1; done[a+1][b]+=1;
        if(isPossible(a,b+1) && isPossible(a+1,b)){
            dfs(curr+toAdd,a+1,0);
        }
        done[a][b+1]-=1; done[a+1][b]-=1;

        toAdd = 0;
        if(done[a][b] == 0){
            toAdd += matrix[a][b];
        }
        if(done[a+1][b+1] == 0){
            toAdd += matrix[a+1][b+1];
        }
        done[a][b]+=1; done[a+1][b+1]+=1;
        if(isPossible(a,b) && isPossible(a+1,b+1)){
            dfs(curr+toAdd,a+1,0);
        }
        done[a][b]-=1; done[a+1][b+1]-=1;
    }
}
int main() {
    cin >> N;
    for(int i = 0; i < N; i+=1){
        for(int j = 0; j < N; j+=1){
            cin >> matrix[i][j];
            done[i][j] = 0;
        }
    }
    dfs(0,0,0);
    cout << best;
    return 0;
}
