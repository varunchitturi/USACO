#include <iostream>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <vector>
using namespace std;

struct command{int day;int id;int change;};
bool commandCompare(const command &a, const command &b)
{
    return a.day < b.day;
}
int main(){
    int numCommands;
    int base;
    cin >> numCommands >> base;
    unordered_map<int, int> IDvalue;
    map<int,unordered_set<int>> valueID;
    vector<command> allCommands;
    unordered_set<int> ids;
    for(int i = 0; i< numCommands;i++){
        int day; int id; int change;
        cin >> day >> id >> change;
        command toAdd;
        toAdd.day = day; toAdd.id = id; toAdd.change = change;
        allCommands.push_back(toAdd);
        ids.insert(id);
    }
    unordered_set<int> mySet;
    mySet.insert(-1);
    valueID.insert(make_pair(base, mySet));
    for(int elem: ids){
        IDvalue.insert(make_pair(elem,base));
    }
    IDvalue.insert(make_pair(-1, base));
    int answer = 0;
    sort(allCommands.begin(),allCommands.end(),commandCompare);
    for(int i = 0; i< allCommands.size();i++){
        int currentValue = IDvalue[allCommands[i].id];
        int currentMax = (*(valueID.rbegin())).first;
        int currentMaxSize = valueID[currentMax].size();
        int currentSize = valueID[currentValue].size();
        int newValue = currentValue + allCommands[i].change;
        bool isCurrentBest = false;
        if(currentValue == currentMax){
            isCurrentBest = true;
        }
        if(currentSize == 1){
            valueID.erase(currentValue);
        }
        else{
            valueID[currentValue].erase(allCommands[i].id);
        }
        if(valueID.find(newValue) != valueID.end()){
            valueID[newValue].insert(allCommands[i].id);
        }
        else{
            unordered_set<int> mySet;
            mySet.insert(allCommands[i].id);
            valueID.insert(make_pair(newValue,mySet));
        }
        int newMax = (*(valueID.rbegin())).first;
        int newSize = valueID[newMax].size();
        bool isNewBest = false;
        if(newValue == newMax){
            isNewBest = true;
        }
        IDvalue[allCommands[i].id] = newValue;
        if(currentMax == newMax && currentMaxSize != newSize){
            answer++;
        }
        else if((isNewBest && !isCurrentBest) || (isCurrentBest && !isNewBest)) {
            answer++;
        }
        else if(isNewBest && isCurrentBest && (currentMaxSize != 1 || newSize != 1)){
            answer++;
        }

    }
    cout << answer+1;




    return 0;
}

