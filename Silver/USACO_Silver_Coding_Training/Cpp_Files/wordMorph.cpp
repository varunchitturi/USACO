#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <unordered_set>
#include <queue>
using namespace std;
struct queueElement{
    string str; int count;
};
char letters [26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
//vector<char> letters;
int main() {
    string first,second;
    cin >> first >> second;
    unordered_set<string> set;
    string current;
    getline(cin,current);
    while(getline(cin,current)){
        if(current == ""){
            break;
        }
        if(current.size() == first.size()) {
            set.insert(current);
        }

    }
    //for(int i = 0; i < second.size();i++){
  //      letters.push_back(second[i]);
   // }
    queue<queueElement> q;
    queueElement e; e.str = first;e.count = 0;
    q.push(e);
    while(!q.empty()){
        if(q.front().str == second){
            cout << q.front().count;
            exit(0);
        }
        for(int j = 0; j < q.front().str.size();j++){
                //if(q.front().str[j] != second[j]){
                    for(int k = 0; k < 26;k++) {
                        queueElement toAdd;
                        toAdd.str = q.front().str; toAdd.count = q.front().count+1;
                        toAdd.str[j] = letters[k];
                        if(set.find(toAdd.str) != set.end()){
                            q.push(toAdd);
                            set.erase(toAdd.str);
                        }
                    }
                //}
            }
        q.pop();
    }

    return 0;
}