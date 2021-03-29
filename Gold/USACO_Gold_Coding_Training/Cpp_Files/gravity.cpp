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

string grid [500];

struct coord{
    int i,j;
};
struct qElement{
    int direction, timesFlipped, i, j;
    qElement(int direction, int timesFlipped, int i, int j) : direction(direction), timesFlipped(timesFlipped), i(i),
                                                              j(j) {}
    bool operator<(const qElement &o) const
    {
        return timesFlipped > o.timesFlipped;
    }

};
int main() {
    int n, m;
    coord capInit;
    bool gotCap = false;
    cin >> m >> n;
    for(int i = 0; i < m; i++){
        string curr; cin >> curr;
        grid[i] = curr;
        if(!gotCap){
            for(int j = 0; j < curr.size(); j++){
                if(curr[j] == 'C'){
                    gotCap = true;
                    capInit.i = i;
                    capInit.j = j;
                }
            }
        }
    }

        priority_queue<qElement> q;
        int visitedUp [500][500] = {0};
        int visitedDown [500][500] = {0};
        q.push(qElement(-1,0,capInit.i,capInit.j));
        while(!q.empty()){
            qElement front = q.top();
            if(front.i >= 0 && front.i < m && front.j >= 0 && front.j < n && grid[front.i][front.j] != '#' ){
                if(grid[front.i][front.j] == 'D'){
                    cout << front.timesFlipped;
                    return 0;
                }
                if(front.direction == 1){
                    if(visitedUp[front.i][front.j] == 0){
                        visitedUp[front.i][front.j]++;
                        if(front.i != 0 && grid[front.i-1][front.j] == '#'){
                            q.push(qElement(1,front.timesFlipped, front.i, front.j+1));
                            q.push(qElement(1,front.timesFlipped, front.i, front.j-1));
                            q.push(qElement(-1,front.timesFlipped+1, front.i+1, front.j));
                        }
                        else if(front.i != 0 && grid[front.i-1][front.j] == '.'){
                            q.push(qElement(1,front.timesFlipped,front.i-1,front.j));
                        }
                        else if(front.i != 0 && grid[front.i-1][front.j] == 'D'){
                            cout << front.timesFlipped;
                            return 0;
                        }
                    }
                }
                else {
                    if(visitedDown[front.i][front.j] == 0){
                        visitedDown[front.i][front.j]++;
                        if(front.i != m && grid[front.i+1][front.j] == '#'){
                            q.push(qElement(-1,front.timesFlipped, front.i, front.j+1));
                            q.push(qElement(-1,front.timesFlipped, front.i, front.j-1));
                            q.push(qElement(1,front.timesFlipped+1, front.i-1, front.j));
                        }
                        else if(front.i != m && grid[front.i+1][front.j] == '.'){
                            q.push(qElement(-1,front.timesFlipped,front.i+1,front.j));
                        }
                        else if(front.i != m && grid[front.i+1][front.j] == 'D'){
                            cout << front.timesFlipped;
                            return 0;
                        }
                    }

                }
            }
            q.pop();
        }


    cout << -1;
    return 0;
}
