//
// Created by Varun Chitturi on 9/30/20.
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

int w, h;
char grid [201][77];
char newGrid[201][77];
int m = 1;

struct qElement{
    int steps,i,j;
    qElement(int steps, int i, int j) : steps(steps), i(i), j(j) {}

};
queue<qElement> q;
bool check(const int i, const int j){
    if((i == 1 && grid[i-1][j] == ' ') || (i==2*h-1 && grid[i+1][j] ==' ') || (j == 1 && grid[i][j-1] == ' ') || (j == 2*w-1 && grid[i][j+1] == ' ')){
        return true;
    }
    return false;
}

void floodfill(const int i, const int j){
    while(!q.empty()){
        q.pop();
    }
    qElement init(0,i,j);
    q.push(init);

    for(int i = 0; i < 2*h+1;i++){
        for(int j = 0; j < 2*w+1;j++){
            newGrid[i][j] = grid[i][j];
        }
    }
    while(!q.empty()){
        qElement front = q.front();
        if(front.i >= 0 && front.i < 2*h+1 && front.j >= 0 && front.j < 2*w+1 && newGrid[front.i][front.j] == ' '){
            if(check(front.i,front.j)){
                if(front.steps+1 > m){
                    m = front.steps + 1;
                }
                return;
            }
            newGrid[front.i][front.j] = '*';
            if(front.i >= 0 && front.i < 2*h+1 && front.j >= 0 && front.j < 2*w+1 && newGrid[front.i-1][front.j] == ' ' && front.i-2 >= 0 && newGrid[front.i-2][front.j] == ' '){
                q.push(qElement(front.steps+1,front.i-2,front.j));
            }
            if(front.i >= 0 && front.i < 2*h+1 && front.j >= 0 && front.j < 2*w+1 && newGrid[front.i+1][front.j] == ' ' && front.i+2 < 2*h+1 && newGrid[front.i+2][front.j] == ' '){
                q.push(qElement(front.steps+1,front.i+2,front.j));
            }
            if(front.i >= 0 && front.i < 2*h+1 && front.j >= 0 && front.j < 2*w+1 && newGrid[front.i][front.j+1] == ' ' && front.j+2 < 2*w+1 && newGrid[front.i][front.j+2] == ' '){
                q.push(qElement(front.steps+1,front.i,front.j+2));
            }
            if(front.i >= 0 && front.i < 2*h+1 && front.j >= 0 && front.j < 2*w+1 && newGrid[front.i][front.j-1] == ' ' && front.j+2 >= 0 && newGrid[front.i][front.j-2] == ' '){
                q.push(qElement(front.steps+1,front.i,front.j-2));
            }
        }
        q.pop();
    }

}

int main() {
    cin >> w >> h;

    vector<string> start;
    string in;

    getline(cin, in);
    int num = 0;
    for(int i = 0; i < 2*h+1;i++){
        getline(cin, in);
        for(int j = 0; j < 2*w+1;j++){
            grid[i][j] = in[j];
        }
    }




    for(int i = 1; i < 2*h+1;i+=2){
        for(int j = 1; j < 2*w+1; j+=2){
            if(grid[i][j] == ' '){
                floodfill(i,j);
            }
        }
    }

    cout << m;

    return 0;
}
