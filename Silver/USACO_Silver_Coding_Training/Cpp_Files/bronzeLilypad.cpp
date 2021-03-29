#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;
struct coordinate{
    int i,j;
};
struct queueElement{
    int count;
    int i;
    int j;
};
int matrix[30][30];
int main() {
    int numRows, numColumns, m1, m2;
    coordinate start,end;
    cin >> numRows >> numColumns >> m1 >> m2;
    int lilypad;
    for(int i = 0; i < numRows;i++){
        for(int j = 0; j < numColumns;j++){
            cin >> lilypad;
            matrix[i][j] = lilypad;
            if(lilypad == 3){
                start. i = i; start.j = j;
            }
            else if(lilypad == 4){
                end.i = i; end.j = j;
            }
        }
    }
    queueElement s; s.i = start.i; s.j = start.j; s.count = 0;
    queue<queueElement> q; q.push(s);
    int directionsi [] = {m1,-m1,m1,-m1,m2,-m2,m2,-m2};
    int directionsj [] = {m2,m2,-m2,-m2,m1,m1,-m1,-m1};
    while(!q.empty()){
        queueElement current = q.front();
            if (matrix[q.front().i][q.front().j] == 4) {
                cout << q.front().count;
                exit(0);
            }
            if (matrix[q.front().i][q.front().j] == 1 || matrix[q.front().i][q.front().j] == 3) {
                for(int i = 0; i < 8;i++){
                    queueElement toAdd;
                    toAdd.i = current.i + directionsi[i];
                    toAdd.j = current.j + directionsj[i];
                    toAdd.count = current.count + 1;
                    if(toAdd.i < numRows && toAdd.i >= 0 && toAdd.j < numColumns && toAdd.j >= 0){
                        q.push(toAdd);
                    }
                }
            }

        matrix[current.i][current.j] = 0;
        q.pop();

    }
    return 0;
}