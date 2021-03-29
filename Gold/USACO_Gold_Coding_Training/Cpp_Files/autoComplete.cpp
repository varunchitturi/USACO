//
// Created by Varun Chitturi on 10/4/20.
//

#include <iostream>
#include <string>
#include <algorithm>
#include <utility>
#include <vector>
#include <map>
#include <set>
#include <unordered_set>
#include <queue>
#include <unordered_map>
#include <stack>

using namespace std;
struct p{
    string a; int b;

    p(string a, int b) : a(std::move(a)), b(b) {}
};
bool comp(const p *a, const p *b)
{
    return a->a < b->a;
}
int main() {
    unordered_map<string, unordered_set<int>> mapper;
    
    int autoCount, wordCount;
    vector<p> dict;
    cin >> autoCount >> wordCount;
    string curr;
    for(int i = 0; i < autoCount; i++){
        cin >> curr;
        dict.emplace_back(curr,i);
    }

    vector<p> words;
    unordered_map<string,vector<p *>> shortWords;
    int maxSize = 0;
    for(int i = 0; i < wordCount; i++){
        int num; string autoc;
        cin >> num >> autoc;
        if(autoc.size() > maxSize){
            maxSize = autoc.size();
        }
        shortWords.emplace(autoc, vector<p *>());
        words.emplace_back(autoc,num);
    }
    for(int i = 0; i < autoCount;i++){
        string space;
        for(int j = 0; j < maxSize;j++){
            space += (dict[i].a)[j];
            if(shortWords.find(space) != shortWords.end()){
                shortWords.at(space).insert(shortWords.at(space).begin()+(lower_bound(shortWords.at(space).begin(),shortWords.at(space).end(),&(dict[i]),comp)-shortWords.at(space).begin()), &(dict[i]));
            }
        }
    }

    for(int i = 0; i < wordCount; i++){
        if(words[i].b-1 < shortWords.at(words[i].a).size()){
            cout << ((shortWords.at(words[i].a))[words[i].b-1])->b+1 << "\n";
        }
        else{
            cout << -1 << "\n";
        }
    }
    return 0;
}
