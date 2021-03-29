#include <iostream>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
using namespace std;
int N;
char matrix [18] [18];
int c = 0;
unordered_set<string> complete;
unordered_map<int,unordered_set<string>> middle;
void dfs1(int i, int j, string current){
    current += matrix[i][j];
    if(i+j+1 == N){
        middle[i].insert(current);
        return;
    }
    dfs1(i+1,j,current);
    dfs1(i,j+1,current);
}
void dfs2(int i, int j, string current){
    current += matrix[i][j];
    if(i+j+1 == N){
        if(middle[i].find(current) != middle[i].end() && complete.find(current) == complete.end()){
            c++;
            complete.insert(current);
        }
        return;
    }
    dfs2(i-1,j,current);
    dfs2(i,j-1,current);
}

int main(){
    cin >> N;
    for(int i = 0; i < N;i++) {
        string current; cin >> current;
        for(int j = 0; j < N;j++){
            matrix[i][j] = current[j];
        }
    }
    dfs1(0,0,"");
    dfs2(N-1,N-1,"");
    cout << c;

}
