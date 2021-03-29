
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    string str;
    cin >> str;
    int prefixSum [str.size()];
    int count = 0;
    for(int i = 0; i< str.size();i++){
        if(str[i] == '('){
            count++;
        }
        else{
            count--;
        }
        prefixSum[i] = count;
    }
    int total = 0;
    if(prefixSum[str.size()-1] == -2){
        for(int i = 0; i < str.size();i++){
            if(prefixSum[i] == -1 && str[i] == ')'){
                total++;
                break;
            }
            else if(str[i] == ')'){
                total++;
            }

        }
    }
    else{

        for(int i = 0; i < str.size();i++){
            if(str[i] == '('){
                str[i] = ')';
            }
            else{
                str[i] = '(';            }
        }
        reverse(str.begin(),str.end());
        count = 0;
        for(int i = 0 ;i < str.size();i++){
            if(str[i] == '('){
                count++;
            }
            else{
                count--;
            }
            prefixSum[i] = count;
        }
        if(prefixSum[str.size()-1] == -2){
            for(int i = 0; i < str.size();i++){
                if(prefixSum[i] == -1 && str[i] == ')'){
                    total++;
                    break;
                }
                else if(str[i] == ')'){
                    total++;
                }

            }
        }}
    cout << total;
}
