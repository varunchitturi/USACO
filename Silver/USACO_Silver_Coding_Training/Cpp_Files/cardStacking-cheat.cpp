//
// Created by Varun Chitturi on 5/28/20.
//



#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    int N,K,P;
    cin >> N >> K >> P;
    vector<int> cards;
    vector<int> bessieCards;
    for(int i = 0; i < K;i++){
        cards.push_back(i+1);
    }
    int count = 0;
    int i = 0;
    int cardsDone = P;
    while(cards.size()!=0){

        count++;
        if(count == N){
            bessieCards.push_back(cards[i]);
            cards.erase(cards.begin()+i);
            count = 0;
            cardsDone = 0;



        }
        else{
            cards.erase(cards.begin()+i);

            cardsDone = 0;

        }

        if(cards.size()!= 0)
            i = (i+P)%cards.size();
    }
    sort(bessieCards.begin(),bessieCards.end());
    for(int i = 0; i < bessieCards.size();i++){
        cout << bessieCards[i] << "\n";
    }
}
