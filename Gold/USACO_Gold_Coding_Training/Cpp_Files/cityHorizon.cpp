//
// Created by Varun Chitturi on 10/19/20.
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

struct b{
    long long index, height, x;
   bool isStart;
    b(long long index, long long height, long long x, bool isStart) : index(index), height(height), x(x), isStart(isStart) {}

};
struct height{
    int index, h;
    height(long long index, long long h) : index(index), h(h) {}
};
bool cmp(const b& a, const b& b) {
    if(a.x == b.x){
        return !a.isStart;
    }
    return a.x < b.x;
}
bool cmp2(const height& a, const height& b) {
    return a.h < b.h;
}
void ins(vector<height> * a,height b){
    a->insert(lower_bound(a->begin(),a->end(),b,cmp2),b);
}
void rem(vector<height> * a,height b){
    a->erase(lower_bound(a->begin(),a->end(),b,cmp2));
}
int main() {
    int n; cin >> n;
    vector<b> buildings;
    unordered_map<int,int> indexPos;
    for(int i = 0; i < n; i++){
        int x1,x2,h; cin >> x1 >> x2 >> h;
        buildings.emplace_back(i,h,x1,true);
        buildings.emplace_back(i,h,x2,false);
        indexPos.emplace(i,x1);
    }
    sort(buildings.begin(), buildings.end(),cmp);
    vector<height> heights;
    long long ans = 0;
    long long currentIndex = buildings[0].index;
    long long currentHeight = buildings[0].height;
    long long currentStart = buildings[0].x;
    ins(&heights,height(currentIndex,currentHeight));

    for(int i = 1; i < buildings.size(); i++){
        if(heights.empty()){
            currentStart = buildings[i].x;
            ins(&heights,height(buildings[i].index,buildings[i].height));
        }

        else if(buildings[i].isStart){
            if(buildings[i].height == heights[heights.size()-1].h){
                ans += (buildings[i].x-currentStart) * heights[heights.size()-1].h;
                currentStart = buildings[i].x;
                ins(&heights,height(buildings[i].index,buildings[i].height));
            }
            else if(buildings[i].height < heights[heights.size()-1].h){
                ins(&heights,height(buildings[i].index,buildings[i].height));
            }
            else{
                ans += (buildings[i].x-currentStart) * heights[heights.size()-1].h;
                currentStart = buildings[i].x;
                ins(&heights,height(buildings[i].index,buildings[i].height));
            }

        }
        else{
            if(buildings[i].height == heights[heights.size()-1].h){
                ans += (buildings[i].x-currentStart) * heights[heights.size()-1].h;
                currentStart = buildings[i].x;
                rem(&heights,height(buildings[i].index,buildings[i].height));
            }
            else if(buildings[i].height < heights[heights.size()-1].h){
                rem(&heights,height(buildings[i].index,buildings[i].height));

            }
            else{
                ans += (buildings[i].x-currentStart) * heights[heights.size()-1].h;
                currentStart = buildings[i].x;
                rem(&heights,height(buildings[i].index,buildings[i].height));
            }
        }


    }
    cout << ans;
    return 0;
}
