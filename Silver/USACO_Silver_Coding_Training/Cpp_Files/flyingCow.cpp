
#include <iostream>
#include <queue>


using namespace std;

int main() {
    struct farm{
        int location,energy;

    };
    queue<farm> all;
    int usedPos [1000005] = {0};
    int N;
    cin >> N;
    farm start = {1,0};
    all.push(start);
    while(true){
        if(all.front().location == N){
            cout << all.front().energy;
            break;
        }
        if(all.front().location > 0 && all.front().location-1-N <= 3 && usedPos[all.front().location-1] == 0 && all.front().location-1 < 1000004){
            all.push(farm {all.front().location-1, all.front().energy+1});
            usedPos[all.front().location-1] = 1;
        }
        if(all.front().location+1 < 1000004 && all.front().location < N && usedPos[all.front().location+1] == 0 ){
            all.push(farm {all.front().location+1, all.front().energy+1});
            usedPos[all.front().location+1] = 1;
        }
        if(all.front().location*3 < 1000004 && all.front().location < N && usedPos[all.front().location*3] == 0 ){
            all.push(farm {all.front().location*3, all.front().energy+1});
            usedPos[all.front().location*3] = 1;
        }
        all.pop();
    }

}

