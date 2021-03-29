//
// Created by Varun Chitturi on 9/16/20.
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
struct coordinate{
    int x; int y;
};
struct qElement{
    coordinate c;
    int balesRemoved;
};
string convert(coordinate a){
    string toReturn; toReturn += a.x;
    toReturn += " ";
    toReturn += a.y;
    return toReturn;
}
int main() {
    int bales [1002][1002] = {0};
    int numBales, x1, y1;
    cin >> numBales >> x1 >> y1;
    vector<coordinate> baleCoordinates;
    baleCoordinates.reserve(numBales);
    for(int i = 0; i < numBales; i++){
        int x,y;
        cin >> x >> y;
        baleCoordinates.push_back(coordinate{x,y});
       bales[x][y] = 1;
    }
    queue<qElement> q;
    qElement start = {x1,y1,0};
    for(int i = 0; i < numBales+1;i++){
        q = queue<qElement>();
        q.push(start);
        bool encountered [1002][1002] = {false};
        while(!q.empty()){
            if(q.front().c.x == 1 && q.front().c.y == 1){
                cout << q.front().balesRemoved;
                return 0;
            }
            if(q.front().balesRemoved <= i && q.front().c.x <= 1001 && q.front().c.y <= 1001 && q.front().c.x >= 0 && q.front().c.y >= 0 && !encountered[q.front().c.x][q.front().c.y]){
                encountered[q.front().c.x][q.front().c.y] = true;
                qElement toAdd;
                toAdd.c.x = q.front().c.x+1; toAdd.c.y = q.front().c.y;
                toAdd.balesRemoved = q.front().balesRemoved;
                if(toAdd.c.x >= 0 && toAdd.c.y >= 0 && toAdd.c.x <= 1000 && toAdd.c.y <= 1000 && bales[toAdd.c.x][toAdd.c.y] == 1){
                    toAdd.balesRemoved++;
                }
                q.push(toAdd);
                toAdd.c.x = q.front().c.x-1; toAdd.c.y = q.front().c.y;
                toAdd.balesRemoved = q.front().balesRemoved;
                if(toAdd.c.x >= 0 && toAdd.c.y >= 0 && toAdd.c.x <= 1000 && toAdd.c.y <= 1000 && bales[toAdd.c.x][toAdd.c.y] == 1){
                    toAdd.balesRemoved++;
                }
                q.push(toAdd);
                toAdd.c.x = q.front().c.x; toAdd.c.y = q.front().c.y+1;
                toAdd.balesRemoved = q.front().balesRemoved;
                if(toAdd.c.x >= 0 && toAdd.c.y >= 0 && toAdd.c.x <= 1000 && toAdd.c.y <= 1000 && bales[toAdd.c.x][toAdd.c.y] == 1){
                    toAdd.balesRemoved++;
                }
                q.push(toAdd);
                toAdd.c.x = q.front().c.x; toAdd.c.y = q.front().c.y-1;
                toAdd.balesRemoved = q.front().balesRemoved;
                if(toAdd.c.x >= 0 && toAdd.c.y >= 0 && toAdd.c.x <= 1000 && toAdd.c.y <= 1000 && bales[toAdd.c.x][toAdd.c.y] == 1){
                    toAdd.balesRemoved++;
                }
                q.push(toAdd);

            }
            q.pop();
        }
    }
}
