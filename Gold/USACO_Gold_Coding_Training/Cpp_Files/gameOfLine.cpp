//
// Created by Varun Chitturi on 10/15/20.
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

struct coord{
    int x,y;

    coord(int x, int y) : x(x), y(y) {}
};
unordered_set<double> slope;

void getSlope(coord curr1, coord curr2){
    if(curr1.x-curr2.x == 0){
        slope.insert(999999999999);
        return;
    }
    slope.insert(((double)(curr1.y-curr2.y))/(double)(curr1.x-curr2.x));
}


int main() {

    int n; cin >> n;
    vector<coord> coords;
    for(int i = 0; i < n; i++){
        int x,y; cin >> x >> y;
        coords.emplace_back(x,y);
    }
    for(int i = 0; i < n-1;i++){
        for(int j = i+1; j < n; j++){
            getSlope(coords[i],coords[j]);
        }
    }
    cout << slope.size();


    return 0;
}
