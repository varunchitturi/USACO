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
int N;
int matrix[100][100][100];
int MAX = 0;
struct stackElement{
    int i,j,k;
};
void dfs(int i , int j, int k){
    stack<stackElement> a;
    stackElement e; e.i = i; e.j = j; e.k = k;
    a.push(e);
    matrix[i][j][k] = -1;
    while(!a.empty()) {
        stackElement curr;
        curr.i = a.top().i; curr.j = a.top().j; curr.k = a.top().k;
        a.pop();
        int b = curr.i; int c = curr.j; int d = curr.k;
        matrix[curr.i][curr.j][curr.k] = -1;
        if (b > 0 && matrix[b - 1][c][d] == 1) {
            //dfs(i-1,j,k);
            e.i = curr.i-1; e.j = curr.j; e.k = curr.k;
            a.push(e);
        }
        if (b < N - 1 && matrix[b + 1][c][d] == 1) {
            //dfs(i + 1, j, k);
            e.i = curr.i+1; e.j = curr.j; e.k = curr.k;
            a.push(e);
        }
        if (c > 0 && matrix[b][c - 1][d] == 1) {
            //dfs(i, j - 1, k);
            e.i = curr.i; e.j = curr.j-1; e.k = curr.k;

            a.push(e);
        }
        if (c < N - 1 && matrix[b][c + 1][d] == 1) {
            //dfs(i, j + 1, k);
           e.i = curr.i; e.j = curr.j+1; e.k = curr.k;

           a.push(e);
        }
        if (d > 0 && matrix[b][c][d - 1] == 1) {
            //dfs(i, j, k - 1);
            e.i = curr.i; e.j = curr.j; e.k = curr.k-1;
            a.push(e);
        }
        if (d < N - 1 && matrix[b][c][d + 1] == 1) {
            //dfs(i, j, k + 1);
            e.i = curr.i; e.j = curr.j; e.k = curr.k+1;
            a.push(e);
        }
    }


}
int main() {
    cin >> N;
    for(int i = 0; i < N;i++){
        for(int j = 0; j < N; j++){
            string in; cin >> in;
            for(int k = 0; k < N; k++){
                if(in[k] == '.'){
                    matrix[i][j][k] = 0;
                }
                else{
                    matrix[i][j][k] = 1;
                }

            }
        }
    }
    for(int i = 0 ; i < N; i++){
        for(int j = 0 ; j < N; j++){
            for(int k = 0; k < N; k++){
                if(matrix[i][j][k] == 1){
                    MAX++;
                    dfs(i,j,k);
                }
                else{
                    //matrix[i][j][k] = -1;
                }
            }
        }
    }
    cout << MAX;


    return 0;
}