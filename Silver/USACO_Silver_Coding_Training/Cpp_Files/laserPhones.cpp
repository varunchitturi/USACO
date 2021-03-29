#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;
int W,H;
vector<vector<int>> matrix;
struct queueElement{
    int i; int j; int numMirrors; int direction; int ignore;
    /*
     0 = >
     1 = <
     2 = up
     3 = down
     */

};
void print(vector<vector<int>>a){
    for(int i = 0; i< H;i++){
        for(int j = 0; j < W; j++){
            cout << a[i][j] << "\t";
        }
        cout << "\n";
    }
}

int main() {
    cin >> W >> H;
    char in;
    int count = 0;
    // input
    int startI;
    int startJ;
    for(int i = 0; i < H;i++){
        vector<int> toAdd;
        for (int j = 0; j < W; ++j) {
            cin >> in;
            if(in == '.'){
                toAdd.push_back(0);
            }
            else if(in == '*'){
                toAdd.push_back(-1);
            }
            else{
                if(count == 0){
                    toAdd.push_back(-1);
                    startI = i; startJ = j;
                    count++;
                }
                else{
                    toAdd.push_back(1);
                }


            }

        }
        matrix.push_back(toAdd);
    }

    //bfs
    /*
     0 = >
     1 = <
     2 = up
     3 = down
     */
    queue<queueElement> queue;
    queueElement add; add.i = startI; add.j = startJ; add.direction = 0;add.numMirrors = 0;add.ignore = 5;
    queue.push(add);
    add; add.i = startI; add.j = startJ; add.direction = 1; add.numMirrors = 0;add.ignore = 5;
    queue.push(add);
    add; add.i = startI; add.j = startJ; add.direction = 2;add.numMirrors = 0;add.ignore = 5;
    queue.push(add);
    add; add.i = startI; add.j = startJ; add.direction = 3;;add.numMirrors = 0;add.ignore = 5;
    queue.push(add);

    while(!queue.empty()){
        if(queue.front().direction == 0){
            queueElement toAdd;
            queueElement toAdd1;
            for(int i = queue.front().j+1; i < W;i++){
                if(matrix[queue.front().i][i] == 1){
                    cout << queue.front().numMirrors;
                    exit(0);
                }
                if(matrix[queue.front().i][i] == 0 || (matrix[queue.front().i][i] >= queue.front().ignore && matrix[queue.front().i][i] != -1)){
                    matrix[queue.front().i][i] = queue.front().ignore;
                    toAdd.i = queue.front().i; toAdd.j = i;; toAdd.direction = 2; toAdd.numMirrors = queue.front().numMirrors+1; toAdd.ignore = queue.front().ignore+1;
                    toAdd1.i = queue.front().i; toAdd1.j = i; toAdd1.direction = 3;toAdd1.numMirrors = queue.front().numMirrors+1;toAdd1.ignore = queue.front().ignore+1;
                    queue.push(toAdd);
                    queue.push(toAdd1);
                }
                else if(matrix[queue.front().i][i] == -1 || matrix[queue.front().i][i] < queue.front().ignore){
                    break;
                }


            }
            queue.pop();

        }
        else if(queue.front().direction == 1){
            queueElement toAdd;
            queueElement toAdd1;
            for(int i = queue.front().j-1; i >= 0;i--){
                if(matrix[queue.front().i][i] == 1){
                    cout << queue.front().numMirrors;
                    exit(0);
                }

                if(matrix[queue.front().i][i] == 0 || (matrix[queue.front().i][i] >= queue.front().ignore && matrix[queue.front().i][i] != -1)){
                    matrix[queue.front().i][i] = queue.front().ignore;
                    toAdd.i = queue.front().i; toAdd.j = i;; toAdd.direction = 2; toAdd.numMirrors = queue.front().numMirrors+1;toAdd.ignore = queue.front().ignore+1;
                    toAdd1.i = queue.front().i; toAdd1.j = i; ; toAdd1.direction = 3;toAdd1.numMirrors = queue.front().numMirrors+1;toAdd1.ignore = queue.front().ignore+1;
                    queue.push(toAdd);
                    queue.push(toAdd1);
                }
                else if(matrix[queue.front().i][i] == -1 || matrix[queue.front().i][i] < queue.front().ignore){
                    break;
                }


            }
            queue.pop();
        }
        else if(queue.front().direction == 2){
            queueElement toAdd;
            queueElement toAdd1;
            for(int i = queue.front().i-1; i >= 0;i--){
                if(matrix[i][queue.front().j] == 1 ){
                    cout << queue.front().numMirrors;
                    exit(0);
                }
                if(matrix[i][queue.front().j] == 0 || (matrix[i][queue.front().j] >= queue.front().ignore && matrix[i][queue.front().j] != -1)){
                    matrix[i][queue.front().j] = queue.front().ignore;
                    toAdd.i = i; toAdd.j = queue.front().j; toAdd.direction = 0; toAdd.numMirrors = queue.front().numMirrors+1;toAdd.ignore = queue.front().ignore+1;
                    toAdd1.i = i; toAdd1.j = queue.front().j;  toAdd1.direction = 1;toAdd1.numMirrors = queue.front().numMirrors+1;toAdd1.ignore = queue.front().ignore+1;
                    queue.push(toAdd);
                    queue.push(toAdd1);
                }
                else if(matrix[i][queue.front().j] == -1 || matrix[i][queue.front().j] < queue.front().ignore){
                    break;
                }
                else{
                    cout << queue.front().numMirrors;
                    exit(0);
                }

            }
            queue.pop();
        }
        else if(queue.front().direction == 3){
            queueElement toAdd;
            queueElement toAdd1;
            for(int i = queue.front().i+1; i < H;i++){
                if(matrix[i][queue.front().j] == 1 ){
                    cout << queue.front().numMirrors;
                    exit(0);
                }
                if(matrix[i][queue.front().j] == 0 || (matrix[i][queue.front().j] >= queue.front().ignore && matrix[i][queue.front().j] != -1)){
                   matrix[i][queue.front().j] = queue.front().ignore;
                    toAdd.i = i; toAdd.j = queue.front().j; toAdd.direction = 0; toAdd.numMirrors = queue.front().numMirrors+1;toAdd.ignore = queue.front().ignore+1;
                    toAdd1.i = i; toAdd1.j = queue.front().j; toAdd1.direction = 1;toAdd1.numMirrors = queue.front().numMirrors+1;toAdd1.ignore = queue.front().ignore+1;
                    queue.push(toAdd);
                    queue.push(toAdd1);
                }
                else if(matrix[i][queue.front().j] == -1 || matrix[i][queue.front().j] < queue.front().ignore){
                    break;
                }


            }
            queue.pop();
        }

        //print(matrix);
        //cout << "\n";
    }

    return 0;
}