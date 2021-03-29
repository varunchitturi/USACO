
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
int real[8];
struct qElement{
    vector<int> config;
    string steps;
};
vector<int> changeA(vector<int> a){

    int temp;
    for(int i = 0; i < 4; i++){
        temp = a[i];
        a[i] = a[7-i];
        a[7-i] = temp;
    }
    return a;
}
vector<int> changeB(vector<int> a){
    int t = a[0];
    a[0] = a[3];
    int t2 = a[1];
    a[1] = t;
    t = a[2];
    a[2] = t2;
    a[3]  = t;

    t = a[7];
    a[7] = a[4];
    t2 = a[6];
    a[6] = t;
    t = a[5];
    a[5] = t2;
    a[4] = t;
    return a;
}
vector<int>  changeC(vector<int> a){
    int t = a[1];
    a[1] = a[6];
    int t2 = a[2];
    a[2] = t;
    t = a[5];
    a[5] = t2;
    a[6] = t;
    return a;
}
string convert(vector<int> a){
    string toReturn;
    for(int i = 0; i < 8; i++){
        toReturn += a[i];
    }
    return toReturn;
}
string convert2(int * a){
    string toReturn;
    for(int i = 0; i < 8; i++){
        toReturn += a[i];
    }
    return toReturn;
}
bool check(vector<int> a){
    for(int i = 0; i < 8; i++){
        if(a[i] != real[i]){
            return false;
        }
    }
    return true;
}
int main(){
    unordered_set<string> encountered;
    vector<int> start;
    int in;
    for(int i = 0; i < 8; i++){
        cin >> in;
        real[i] = in;
        start.push_back(i+1);
    }
    string done = convert2(real);
    qElement first; first.steps=""; first.config = start;
    queue<qElement> q;
    q.push(first);
    while(!q.empty()){
        string current = convert(q.front().config);
        if(current == done){
            cout << q.front().steps.size() << "\n";
            cout << q.front().steps;
            return 0;
        }
        if(encountered.find(current) == encountered.end()){
            encountered.insert(current);
            qElement toAdd; toAdd.config = changeA(q.front().config); toAdd.steps = q.front().steps + "A";
            q.push(toAdd);
            toAdd.config = changeB(q.front().config); toAdd.steps = q.front().steps + "B";
            q.push(toAdd);
            toAdd.config = changeC(q.front().config); toAdd.steps = q.front().steps + "C";
            q.push(toAdd);

        }
        q.pop();
    }



    return 0;
}
