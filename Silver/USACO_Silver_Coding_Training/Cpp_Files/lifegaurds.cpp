#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <unordered_set>
using namespace std;



struct intervalPos{
    int pos;
    bool isStart;
    int index;
};
bool intervalCompare(const intervalPos &a, const intervalPos &b)
{
    return a.pos < b.pos;
}
int main(){
    int N;
    cin >> N;
    vector<intervalPos> allPos;
    map<int,int> log;
    for(int i = 0; i < N;i++){
        int a;
        int b;
        cin >> a >> b;
        intervalPos toAdd1;
        toAdd1.index = i;
        toAdd1.pos = a;
        toAdd1.isStart = true;
        intervalPos toAdd2;
        toAdd2.index = i;
        toAdd2.pos = b;
        toAdd2.isStart = false;
        allPos.push_back(toAdd1);
        allPos.push_back(toAdd2);
    }
    sort(allPos.begin(),allPos.end(),intervalCompare);
    int usefulness[N];
    for(int i= 0; i < N;i++){
        usefulness[i] = 0;
    }

    for(int i= 0 ; i< N*2-1;i++){
        if(allPos[i].isStart){
            if(log.size() == 0){
                log.insert(make_pair(allPos[i].index,allPos[i+1].pos - allPos[i].pos));
                usefulness[allPos[i].index] = allPos[i+1].pos - allPos[i].pos;
            }
            else{
                log.insert(make_pair(allPos[i].index,0));
            }
        }
        else{

            usefulness[allPos[i].index] = log[allPos[i].index];
            log.erase(allPos[i].index);
            if(log.size() == 1){
                int max = (*(log.rbegin())).first;
                log[max] = log[max] +  allPos[i+1].pos - allPos[i].pos;
                usefulness[max] = log[max];
            }
        }
    }
    int minIndex = 0;
    double min = usefulness[0];
    for(int i = 0; i< N;i++){
        if(min > usefulness[i]){
            min = usefulness[i];
            minIndex = i;
        }
    }

    vector<intervalPos> finalIntervalPos;

    for(int i= 0 ; i< N*2;i++){
        if(allPos[i].index != minIndex){
            finalIntervalPos.push_back(allPos[i]);

        }
    }
    //System.out.println();
    //System.out.println(Arrays.toString(usefulness));
    // System.out.println(Arrays.toString(ratios));
    //System.out.println();
    int totalDistance = 0;
    unordered_set<int> indexes;
    for(int i = 0 ; i < finalIntervalPos.size()-1;i++){

        if(finalIntervalPos[i].isStart){
            indexes.insert(finalIntervalPos[i].index);
            if(indexes.size() != 0){
                totalDistance += finalIntervalPos[i+1].pos - finalIntervalPos[i].pos;
            }
        }
        else{
            indexes.erase(finalIntervalPos[i].index);
            if(indexes.size() != 0){
                totalDistance += finalIntervalPos[i+1].pos - finalIntervalPos[i].pos;
            }
        }

    }
    cout << totalDistance << "\n";
    /*
     for(int i = 0; i < N;i++){
         cout << usefulness[i] << " ";
     }
 */


    return 0;
}
