#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;
struct cell{
    int mineCount;
    bool isMine;
    int i;
    int j;
};
struct coordinates{
    int i;
    int j;
};
int numRows;
int numColumns;
int numMines;
cell matrix [30][30];
vector<cell> getEmptyCells( int i, int j){
    vector<cell> toReturn;
    if(i == 0 && j == 0 && !matrix[i][j].isMine){
        toReturn.push_back(matrix[i][j]);
    }
    if( j == 0 && i+1 != numRows && !matrix[i+1][j].isMine){
        toReturn.push_back(matrix[i+1][j]);
    }

    if(i == 0 && j+1 != numColumns && !matrix[i][j+1].isMine){
        toReturn.push_back(matrix[i][j+1]);
    }
    if(i+1 != numRows && j +1 != numColumns && !matrix[i+1][j+1].isMine){
        toReturn.push_back(matrix[i+1][j+1]);
    }

    return toReturn;
}
int getFilledCellCount(int i,int j){
    int count = 0;
    if(matrix[i][j].isMine){
        count++;
    }
    if(i != 0 && matrix[i-1][j].isMine){
        count++;
    }
    if(i+1 != numRows && matrix[i+1][j].isMine){
        count++;
    }
    if(j!=0 && matrix[i][j-1].isMine){
        count++;
    }
    if(j+1 != numColumns && matrix[i][j+1].isMine){
        count++;
    }
    if(i != 0 && j != 0 && matrix[i-1][j-1].isMine){
        count++;
    }
    if(i!=0 && j+1 != numColumns && matrix[i-1][j+1].isMine){
        count++;
    }
    if(i+1 != numRows && j != 0 && matrix[i+1][j-1].isMine){
        count++;
    }
    if(i+1 != numRows && j +1 != numColumns && matrix[i+1][j+1].isMine){
        count++;
    }
    return count;
}
void print(){
    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j < numColumns; j++) {
            if (matrix[i][j].isMine){
                cout << (i+1) << " " << (j+1) << "\n";
            }
        }
    }
}
void combinationUtil(vector<vector<cell>> *c,vector<cell> arr, vector<cell> *data, int start, int end, int index, int r) {
    if (index == r)
    {
        vector<cell> toAdd;
        for (int j=0; j<r; j++){
            toAdd.push_back((*data)[j]);
        }
        (*c).push_back(toAdd);
        return;
    }
    for (int i=start; i<=end && end-i+1 >= r-index; i++)
    {
        (*data)[index] = arr[i];
        combinationUtil(c,arr, data, i+1, end, index+1, r);
    }
}
vector<vector<cell>> getCombinations(vector<cell> arr, int r) {
    vector<vector<cell>> c;
    if(r > 0 && arr.size() > 0){
        long n = arr.size();
        vector<cell> data;
        for(int i = 0; i < r;i++){
            cell x;
            data.push_back(x);
        }

        combinationUtil(&c, arr, &data, 0, n-1, 0, r);
        return c;
    }
    return c;
}
bool checkAll(){
    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j < numColumns; j++) {
            int count = 0;
            if(matrix[i][j].isMine){
                count++;
            }
            if(i != 0 && matrix[i-1][j].isMine){
                count++;
            }
            if(i+1 != numRows && matrix[i+1][j].isMine){
                count++;
            }
            if(j!=0 && matrix[i][j-1].isMine){
                count++;
            }
            if(j+1 != numColumns && matrix[i][j+1].isMine){
                count++;
            }
            if(i != 0 && j != 0 && matrix[i-1][j-1].isMine){
                count++;
            }
            if(i!=0 && j+1 != numColumns && matrix[i-1][j+1].isMine){
                count++;
            }
            if(i+1 != numRows && j != 0 && matrix[i+1][j-1].isMine){
                count++;
            }
            if(i+1 != numRows && j +1 != numColumns && matrix[i+1][j+1].isMine){
                count++;
            }
            if(count != matrix[i][j].mineCount){
                return false;
            }

        }
    }
    return true;
}
bool checkAll2(){
    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j < numColumns; j++) {
            int count = 0;
            if(matrix[i][j].isMine){
                count++;
            }
            if(i != 0 && matrix[i-1][j].isMine){
                count++;
            }
            if(i+1 != numRows && matrix[i+1][j].isMine){
                count++;
            }
            if(j!=0 && matrix[i][j-1].isMine){
                count++;
            }
            if(j+1 != numColumns && matrix[i][j+1].isMine){
                count++;
            }
            if(i != 0 && j != 0 && matrix[i-1][j-1].isMine){
                count++;
            }
            if(i!=0 && j+1 != numColumns && matrix[i-1][j+1].isMine){
                count++;
            }
            if(i+1 != numRows && j != 0 && matrix[i+1][j-1].isMine){
                count++;
            }
            if(i+1 != numRows && j +1 != numColumns && matrix[i+1][j+1].isMine){
                count++;
            }
            if(count > matrix[i][j].mineCount){
                return false;
            }

        }
    }
    return true;
}
void undo(coordinates a [],int size){
    for(int i = 0; i< size;i++){
        matrix[a[i].i][a[i].j].isMine = false;
    }
}
void dfs(int i, int j, int mineCount,int doneCount, coordinates c [],int size){
    if(numRows*numColumns - doneCount < numMines-mineCount || i == numRows){
        undo(c,size);
        return;
    }
    if (mineCount == numMines) {
        if (checkAll()) {
            print();
            exit(0);
        } else {
            undo(c,size);
            return;
        }
    }
    vector<cell> emptySurroundingCells = getEmptyCells(i, j);
    int numFilledSurroundingCells = getFilledCellCount(i, j);
    vector<vector<cell>> combinations = getCombinations(emptySurroundingCells, matrix[i][j].mineCount - numFilledSurroundingCells);
    if (combinations.size() != 0) {
        for (int k = 0; k < combinations.size(); k++) {
            coordinates changes [9];
            int count = 0;
            for (int l = 0; l < combinations[k].size(); l++) {
                matrix[combinations[k][l].i][combinations[k][l].j].isMine = true;
                coordinates r;
                r.i = combinations[k][l].i;
                r.j = combinations[k][l].j;
                changes[count++] = r;
            }
            if (checkAll2()) {
                if (j != numColumns - 1) {
                    dfs( i, j + 1, mineCount + matrix[i][j].mineCount - numFilledSurroundingCells,doneCount+1,changes,count);
                    undo(changes,count);
                } else {
                    dfs( i + 1, 0, mineCount + matrix[i][j].mineCount - numFilledSurroundingCells,doneCount+1,changes,count);
                    undo(changes,count);
                }
            }
            else{
                undo(changes,count);
            }


        }
    }

    else{
        coordinates q [9];
        if (j != numColumns - 1) {
            dfs( i, j + 1, mineCount + matrix[i][j].mineCount - numFilledSurroundingCells,doneCount+1,q,0);
        } else {
            dfs( i + 1, 0, mineCount + matrix[i][j].mineCount - numFilledSurroundingCells,doneCount+1,q,0);
        }

    }
}

int main(){
    cin >> numRows>>numColumns>>numMines;
    for(int i = 0; i< numRows;i++){
        for(int j = 0; j< numColumns;j++){
            cell e; e.i = i; e.j = j; e.isMine = false; cin >> e.mineCount;
            matrix[i][j] = e;
        }
    }
    coordinates p [9];
    dfs(0,0,0,0,p,0);
    cout << "NO SOLUTION";





    return 0;
}

