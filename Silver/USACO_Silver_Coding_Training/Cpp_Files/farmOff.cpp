
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
long long N,M,a,b,c,d,e,f,g,h;

bool cmp(pair<int,int> a, pair<int,int> b){
    return(a.first == b.first? a.second < b.second : a.first > b.first);
}
long long powerMod(long long a, long long b, long long c){
    long long factor = 1;
    for(long long i = 0; i < b;i++){
        factor*=a;
        factor %= c;
    }
    return factor;
}
int main(){
    vector<pair<int,int>> allCows;
    long long total = 0;
    cin >> N>>a>>b>>c>>d>>e>>f>>g>>h>>M;
    for(long long i = 0; i<N*3;i++){
        allCows.push_back({(((e*(powerMod(i, 5, h))+f*powerMod(i, 3, h))) +g) %h,(a*powerMod(i, 5, d)+b*powerMod(i, 2, d)+c)%d});
    }
    sort(allCows.begin(),allCows.end(),cmp);
    for(int i = 0; i<N;i++){
        total += allCows[i].second;
        total %= M;
    }

    cout <<total << "\n";
}
