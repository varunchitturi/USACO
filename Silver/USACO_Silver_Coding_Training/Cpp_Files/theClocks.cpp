#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <unordered_set>
#include <queue>
#include <unordered_map>

using namespace std;
vector<vector<int>> matrix;
unordered_set<string> visited;
string toString(vector<int> m){
    string a = "";
   for(int i  = 0; i < 9; i++){
       for(int j = 0; j < m[i];j++){
           a += to_string(i+1); a+= " ";
       }
   }
    return a;
}
struct queueElement{
    vector<int> moves;
    vector<vector<int>> m;
};
bool check(vector<vector<int>>  m){
    for(int i = 0; i < 3;i++){
        for(int j = 0; j <3 ;j++){
            if(m[i][j] != 12){
                return false;
            }
        }
    }
    return true;
}
void move1(vector<vector<int>> * m){
    (*m)[0][0] = ((*m)[0][0]%12)+3;
    (*m)[0][1] = ((*m)[0][1]%12)+3;
    (*m)[1][0] = ((*m)[1][0]%12)+3;
    (*m)[1][1] = ((*m)[1][1]%12)+3;
};
void move2(vector<vector<int>> * m){
    (*m)[0][0] = ((*m)[0][0]%12)+3;
    (*m)[0][1] = ((*m)[0][1]%12)+3;
    (*m)[0][2] = ((*m)[0][2]%12)+3;

};
void move3(vector<vector<int>> * m){
    (*m)[0][1] = ((*m)[0][1]%12)+3;
    (*m)[0][2] = ((*m)[0][2]%12)+3;
    (*m)[1][1] = ((*m)[1][1]%12)+3;
    (*m)[1][2] = ((*m)[1][2]%12)+3;
};
void move4(vector<vector<int>> * m){
    (*m)[0][0] = ((*m)[0][0]%12)+3;
    (*m)[1][0] = ((*m)[1][0]%12)+3;
    (*m)[2][0] = ((*m)[2][0]%12)+3;
};
void move5(vector<vector<int>> * m){
    (*m)[0][1] = ((*m)[0][1]%12)+3;
    (*m)[1][0] = ((*m)[1][0]%12)+3;
    (*m)[1][1] = ((*m)[1][1]%12)+3;
    (*m)[1][2] = ((*m)[1][2]%12)+3;
    (*m)[2][1] = ((*m)[2][1]%12)+3;
};
void move6(vector<vector<int>> * m){
    (*m)[0][2] = ((*m)[0][2]%12)+3;
    (*m)[1][2] = ((*m)[1][2]%12)+3;
    (*m)[2][2] = ((*m)[2][2]%12)+3;
};
void move7(vector<vector<int>> * m){
    (*m)[1][0] = ((*m)[1][0]%12)+3;
    (*m)[1][1] = ((*m)[1][1]%12)+3;
    (*m)[2][0] = ((*m)[2][0]%12)+3;
    (*m)[2][1] = ((*m)[2][1]%12)+3;
};
void move8(vector<vector<int>> * m){
    (*m)[2][0] = ((*m)[2][0]%12)+3;
    (*m)[2][1] = ((*m)[2][1]%12)+3;
    (*m)[2][2] = ((*m)[2][2]%12)+3;
};
void move9(vector<vector<int>> * m){
    (*m)[1][1] = ((*m)[1][1]%12)+3;
    (*m)[1][2] = ((*m)[1][2]%12)+3;
    (*m)[2][1] = ((*m)[2][1]%12)+3;
    (*m)[2][2] = ((*m)[2][2]%12)+3;
};
vector<vector<int>> allComb;
void dfs(vector<int> comb){
  for(int j = 0; j < 4;j++){
      comb.push_back(j);
      if(comb.size() == 9){
          allComb.push_back(comb);
      }
      else{
          dfs(comb);
      }
      comb.pop_back();
  }
}
int main() {
    int in;
    for(int i = 0; i < 3;i++){
        vector<int> a;
        for(int j = 0; j < 3;j++){
            cin >> in;
            a.push_back(in);
        }
        matrix.push_back(a);
    }
    vector<int> start;
    dfs(start);
    vector<string> solutions;
    for(int i = 0; i < allComb.size();i++){
       vector<vector<int>> current = matrix;
       for(int j = 0; j < 9;j++){
           if(j == 0){
               for(int k = 0; k < allComb[i][j];k++){
                   move1(&current);
               }
           }
           else if(j == 1){
               for(int k = 0; k < allComb[i][j];k++){
                   move2(&current);
               }
           }
           else if(j == 2){
               for(int k = 0; k < allComb[i][j];k++){
                   move3(&current);
               }
           }
           else if(j == 3){
               for(int k = 0; k < allComb[i][j];k++){
                   move4(&current);
               }
           }
           else if(j == 4){
               for(int k = 0; k < allComb[i][j];k++){
                   move5(&current);
               }
           }
           else if(j == 5){
               for(int k = 0; k < allComb[i][j];k++){
                   move6(&current);
               }
           }
           else if(j == 6){
               for(int k = 0; k < allComb[i][j];k++){
                   move7(&current);
               }
           }
           else if(j == 7){
               for(int k = 0; k < allComb[i][j];k++){
                   move8(&current);
               }
           }
           else if(j == 8){
               for(int k = 0; k < allComb[i][j];k++){
                   move9(&current);
               }
           }

       }
       if(check(current)){
           solutions.push_back(toString(allComb[i]));
       }

   }
    sort(solutions.begin(),solutions.end());
    cout << *solutions.begin();
}