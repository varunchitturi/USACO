//
// Created by Varun Chitturi on 9/16/20.
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

struct qElement{
    int current;
    int minutes;
};

int main() {
   int farmer, cow;
   cin >> farmer >> cow;
   bool encountered [200001] = {false};
   queue<qElement> q;
   qElement start; start.current = farmer; start.minutes = 0;
   q.push(start);
   while(!q.empty()){
       if(q.front().current == cow){
           cout << q.front().minutes;
           return 0;
       }
       if(q.front().current >= 0 && !encountered[q.front().current] && q.front().current <= 100000){
           encountered[q.front().current] = true;
           qElement toAdd; toAdd.current = q.front().current*2; toAdd.minutes = q.front().minutes+1;
           if(q.front().current < cow) {
               q.push(toAdd);
           }
           toAdd.current /= 2; toAdd.current++;
           if(q.front().current < cow) {
               q.push(toAdd);
           }
           toAdd.current -= 2;
           q.push(toAdd);
       }
       q.pop();
   }

    return 0;
}
