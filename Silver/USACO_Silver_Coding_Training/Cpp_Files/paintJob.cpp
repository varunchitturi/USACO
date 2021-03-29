
#include <iostream>
#include <queue>

using namespace std;
struct  paint{
    int color;
    int numMixes;
};
int main(){

    int bessiePaint;
    int desiredPaint;
    int numBucketsAvailable;
    int numColorTypes;
    queue<paint> all;
    cin >> bessiePaint >> desiredPaint;
    cin >> numBucketsAvailable >> numColorTypes;

    int colorsAvailable [numBucketsAvailable];

    int usedPos [10001] = {0};

    for(int i = 0; i < numBucketsAvailable;i++){
        cin >> colorsAvailable[i];

    }
    all.push(paint {bessiePaint,0 });
    while(all.size() != 0){
        for(int i = 0; i < numBucketsAvailable;i++){
            if(all.front().color == desiredPaint){
                cout << all.front().numMixes;
                return 0;

            }
            if(usedPos[(all.front().color * colorsAvailable[i]) % numColorTypes] == 0){
                all.push(paint {(all.front().color * colorsAvailable[i]) % numColorTypes, all.front().numMixes+1});
                usedPos[(all.front().color * colorsAvailable[i]) % numColorTypes] = 1;
            }

        }
        all.pop();
    }


    cout << -1;







    return 0;

}
