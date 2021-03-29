
#include <iostream>
#include <string>
using namespace std;


int main(){
    string builder = "";
    string toCheck;
    string toDelete;
    cin >> toCheck;
    cin >> toDelete;

    for(int i = 0; i< toCheck.size();i++){
        builder += toCheck[i];
        if(builder.size() >= toDelete.size() && builder.substr(builder.size()-toDelete.size()) == toDelete ){

            builder.resize(builder.size()-toDelete.size());

        }
    }
    cout << builder << "\n";

}


