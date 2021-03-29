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
vector<vector<int>> allComb;
vector<pair<int,int>> coordinates;
unordered_set<int> ys;
int N;

struct coordinate{
    int x,y;
    int isVisited;
    int num;
};
int getNextPortal(vector<coordinate> *a, int j){
    for(int i = 0; i < a->size();i++){
        if(i != j && (*a)[i].num == (*a)[j].num){
            return i;
        }
    }
    return -1;
}
int getNext(vector<coordinate> * a, int currentNum){
    int next = -1;
    int xMin = 2000000000;
    for(int i  = 0; i < a->size();i++){
        if((*a)[i].x > (*a)[currentNum].x && (*a)[i].y == (*a)[currentNum].y && (*a)[i].x < xMin){
            xMin = (*a)[i].x;
            next = i;

        }
    }
    return next;

}
bool isLoop(vector<coordinate> a){

    for(int i = 0; i < a.size();i++){
        int currentNum = i;
        for(int j = 0; j < a.size();j++){
            a[j].isVisited = 0;
        }
        while(true){
            a[currentNum].isVisited++;
            int j = getNext(&a,currentNum);
            if(j == -1){
                break;
            }
            a[j].isVisited++;
            if(a[j].isVisited >= 3){
                return false;
            }
            currentNum = getNextPortal(&a,j);




        }
    }
    return true;
}
bool check(vector<int> a){

        vector<coordinate> b;
        for(int i = 0; i < a.size();i+=2){
            coordinate toAdd1; toAdd1.isVisited = 0; toAdd1.num = i;
            coordinate toAdd2; toAdd2.isVisited = 0; toAdd2.num = i;
            toAdd1.x = coordinates[a[i]].first;toAdd1.y = coordinates[a[i]].second;
            toAdd2.x = coordinates[a[i+1]].first;toAdd2.y = coordinates[a[i+1]].second;
            b.push_back(toAdd1);
            b.push_back(toAdd2);
        }
    return isLoop(b);
}
void makeComb(vector<int> store, vector<int> made){
    if(store.size() == 0){
        allComb.push_back(made);
        return;
    }
    made.push_back(store[0]);
    for(int i = 1; i < store.size();i++){
        vector<int>nextStore = store;
        made.push_back(store[i]);
        nextStore.erase(nextStore.begin()); nextStore.erase(nextStore.begin()+i-1);
        makeComb(nextStore,made);
        made.pop_back();

    }
}

int main() {
    cin >> N;

    vector<int> a;
    for(int i = 0; i < N; i++){
        int x,y; cin >> x >> y;
        coordinates.emplace_back(x,y);
        a.push_back(i);
        ys.insert(y);
    }
    int c = 0;
    makeComb(a,vector<int>());
    for(int i = 0 ; i < allComb.size();i++){
        if(!check(allComb[i])){
            c++;
        }
    }
    cout << c;
    return 0;
}