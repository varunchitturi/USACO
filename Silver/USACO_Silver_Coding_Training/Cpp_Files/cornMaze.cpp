#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <unordered_map>
using namespace std;
struct queueElement{
    int i,j,count;
};
struct coordinates{
    int i,j;
};
struct cPair{
    int starti, startj, endi, endj;
};

int main() {
    int numRows, numColumns;
    cin >> numRows >> numColumns;
    char matrix [300][300];
    coordinates start,end;
    unordered_map<char, cPair> portalMap;
    for(int i = 0 ; i < numRows;i++){
        string into; cin >> into;
        for(int j = 0; j < numColumns;j++){
            char in = into[j];
            if(in  == '#'){
                matrix[i][j] = '5';
            }
            else if(in == '.'){
                matrix[i][j] = '1';
            }
            else if(in == '@'){
                start.i = i, start.j = j;
                matrix[i][j] = '1';
            }
            else if(in == '='){
                end.i = i; end.j = j;
                matrix[i][j] = '2';
            }
            else{
                if(portalMap.find(in) != portalMap.end()){
                    portalMap[in].endi = i; portalMap[in].endj = j;
                    matrix[i][j] = in;
                }
                else{
                    cPair a; a.starti = i; a.startj = j;
                    portalMap[in] = a;
                    matrix[i][j] = in;
                }
            }
        }
    }
    int dirI [] = {1,-1,0,0};
    int dirJ [] = {0,0,1,-1};
    queueElement s; s.count = 0; s.i = start.i; s.j = start.j;
    queue<queueElement> q; q.push(s);
    while(!q.empty()){
        queueElement current = q.front();
        for(int i = 0; i < 4;i++){
            if(current.i+dirI[i] >= 0 && current.i+dirI[i] < numRows && current.j+dirJ[i] >= 0 && current.j+dirJ[i] < numColumns) {
                bool check = true;
                queueElement toAdd;
                if (matrix[current.i + dirI[i]][current.j + dirJ[i]] == '1') {
                    toAdd.i = current.i + dirI[i];
                    toAdd.j = current.j + dirJ[i];
                    toAdd.count = current.count + 1;
                    q.push(toAdd);

                } else if (matrix[current.i + dirI[i]][current.j + dirJ[i]] == '5') {
                    continue;
                } else if (matrix[current.i + dirI[i]][current.j + dirJ[i]] == '2') {
                    cout << current.count + 1;
                    exit(0);
                } else {
                    check = false;
                    if (portalMap.find(matrix[current.i + dirI[i]][current.j + dirJ[i]]) != portalMap.end()) {
                    if (portalMap[matrix[current.i + dirI[i]][current.j + dirJ[i]]].starti == current.i + dirI[i] &&
                        portalMap[matrix[current.i + dirI[i]][current.j + dirJ[i]]].startj == current.j + dirJ[i]) {
                        coordinates toGo;
                        toGo.i = portalMap[matrix[current.i + dirI[i]][current.j + dirJ[i]]].endi;
                        toGo.j = portalMap[matrix[current.i + dirI[i]][current.j + dirJ[i]]].endj;
                        toAdd.i = toGo.i;
                        toAdd.j = toGo.j;
                        toAdd.count = current.count + 1;
                        q.push(toAdd);
                    } else {
                        coordinates toGo;
                        toGo.i = portalMap[matrix[current.i + dirI[i]][current.j + dirJ[i]]].starti;
                        toGo.j = portalMap[matrix[current.i + dirI[i]][current.j + dirJ[i]]].startj;
                        toAdd.i = toGo.i;
                        toAdd.j = toGo.j;
                        toAdd.count = current.count + 1;

                        q.push(toAdd);
                    }
                }
                }
                if(check) {
                    matrix[current.i + dirI[i]][current.j + dirJ[i]] = 5;
                }
            }
        }

        q.pop();
    }
    return 0;
}