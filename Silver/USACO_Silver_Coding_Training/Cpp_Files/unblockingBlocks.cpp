#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <unordered_set>

using namespace std;
vector<pair<int,int>> shape1;
vector<pair<int,int>> shape2;
vector<pair<int,int>> shape3;
int maxx1 = -999999999; int maxy1 = -999999999;
int maxx2 = -99999999; int maxy2 = -99999999;
int maxx3 = -999999999; int maxy3 = -999999999;
int width1,height1,width2,height2,width3,height3; int minx1,miny1,minx2,miny2,minx3,miny3; int anchorx1,anchory1,anchorx2,anchory2,anchorx3,anchory3;
int numShape1, numShape2, numShape3;
struct queueElement{
    int x1x2,y1y2,x1x3,y1y3,numMoves;
    int x2Change,y2Change,x3Change,y3Change;
};

bool noOverlap(queueElement e){
    //compare 1 with 2
    if(maxx1 >= minx2+e.x2Change && maxx2+e.x2Change >= minx1 && maxy1 >= miny2+e.y2Change && maxy2+e.y2Change >= miny1){
        return false;
    }
    else{
        if(maxx1 >= minx3 + e.x3Change && maxx3 + e.x3Change >= minx1 &&   maxy1 >= miny3 + e.y3Change && maxy3 + e.y3Change >= miny1){
            return false;
        }
        else{
            if(maxx2 + e.x2Change >= minx3 + e.x3Change && maxx3 + e.x3Change >= minx2 + e.x2Change && maxy2 + e.y2Change >= miny3 + e.y3Change && maxy3  + e.y3Change>= miny2 + e.y2Change){
                return false;
            }
            else{
                return true;
            }
        }
    }
}
bool isValid(queueElement e){
    unordered_set<string> coordinates;
    for(int i =0; i < numShape1;i++){
        coordinates.insert(to_string(shape1[i].first) + " " + to_string(shape1[i].second));
    }
    for(int i =0; i < numShape2;i++){
        coordinates.insert(to_string(shape2[i].first + e.x2Change) + " " + to_string(shape2[i].second + e.y2Change));
    }
    for(int i =0; i < numShape3;i++){
        coordinates.insert(to_string(shape3[i].first + e.x3Change) + " " + to_string(shape3[i].second + e.y3Change));
    }
    if(coordinates.size() == numShape3 + numShape1 + numShape2){
        return true;
    }
    return false;
}
string getConfig(queueElement e){
    return to_string(e.x1x2) + " " + to_string(e.y1y2) + " " + to_string(e.x1x3) + " " + to_string(e.y1y3);
}
int main(){

    cin >> numShape1 >> numShape2 >> numShape3;
    minx1 =999999999;miny1 = 999999999;
    for(int i = 0; i < numShape1;i++){
        int x, y;cin >> x >> y;
        shape1.emplace_back(x,y);
        if(miny1 > y){
            miny1 = y;
        }
        if(minx1 > x){
            minx1 = x;
            anchorx1 = x;
            anchory1 = y;
        }
        if(maxx1 < x){
            maxx1 = x;
        }
        if(maxy1 < y){
            maxy1 = y;
        }


    }
    width1 = maxx1-minx1; height1 = maxy1-miny1;
    minx2 = 999999999; miny2 = 999999999;
    for(int i = 0; i < numShape2;i++){
        int x, y;cin >> x >> y;
        shape2.emplace_back(x,y);
        if(miny2 > y){
            miny2 = y;
        }
        if(minx2 > x){
            minx2= x;
            anchorx2 = x;
            anchory2 = y;
        }
        if(maxx2 < x){
            maxx2 =x;
        }
        if(maxy2 < y){
            maxy2 = y;
        }
    }
    width2 = maxx2-minx2; height2 = maxy2-miny2;
    minx3 = 999999999; miny3 = 999999999;
    for(int i = 0; i < numShape3;i++){

        int x, y;cin >> x >> y;
        shape3.emplace_back(x,y);
        if(miny3 > y){
            miny3 = y;
        }
        if(minx3 > x){
            minx3 = x;
            anchorx3 = x;
            anchory3 = y;
        }
        if(maxx3 < x){
            maxx3 =x;
        }
        if(maxy3 < y){
            maxy3 = y;
        }
    }
    width3 = maxx3-minx3; height3 = maxy3-miny3;
    queue<queueElement> q;
    unordered_set<string> distances;
    int xdir [4] = {1,-1,0,0};
    int ydir [4] = {0,0,1,-1};
    queueElement start; start.x2Change = 0; start.y2Change = 0; start.x3Change = 0; start.y3Change = 0; start.x1x2 = anchorx1 - anchorx2;
    start.y1y2 = anchory1 - anchory2; start.x1x3 = anchorx1-anchorx3; start.y1y3 = anchory1-anchory3;start.numMoves = 0;
    q.push(start);
    distances.insert(getConfig(start));
    while(!q.empty()){

        if(noOverlap(q.front())){
            cout << q.front().numMoves;
            exit(0);
        }

        for(int i = 1; i <= 3;i++){
            for(int j = 0; j < 4; j++){
                queueElement toAdd = q.front();
                if(i == 1){
                    toAdd.x2Change-= xdir[j];
                    toAdd.x3Change -= xdir[j];
                    toAdd.y2Change -= ydir[j]; toAdd.y3Change -= ydir[j];
                }
                else if( i == 2){
                    toAdd.x2Change += xdir[j];
                    toAdd.y2Change += ydir[j];
                }
                else{
                    toAdd.x3Change += xdir[j];
                    toAdd.y3Change += ydir[j];
                }

                toAdd.numMoves++;
                toAdd.x1x2 = anchorx1 - anchorx2 + toAdd.x2Change;toAdd.y1y2 = anchory1 - anchory2 + toAdd.y2Change;
                toAdd.x1x3 = anchorx1 - anchorx3 + toAdd.x3Change; toAdd.y1y3 = anchory1 -anchory3 + toAdd.y3Change;
                string check  = getConfig(toAdd);
                if(distances.find(check) == distances.end() && isValid(toAdd)   && toAdd.x2Change + anchorx2 >= -30 && toAdd.x2Change+anchorx2+width2 <= 30 && toAdd.x3Change + anchorx3 >= -30 && toAdd.x3Change+anchorx3+width3 <= 30 && anchorx1 >= -30 && anchorx1+width1 <= 30      && toAdd.y2Change + anchory2 >= -30 && toAdd.y2Change+anchory2+height2 <= 30 && toAdd.y3Change + anchory3 >= -30 && toAdd.y3Change+anchory3+height3 <= 30 && anchorx1 >= -30 && anchorx1+height1 <= 30) {
                    distances.insert(check);
                    q.push(toAdd);
                }
            }
        }

    q.pop();
    }
    cout << -1;
}