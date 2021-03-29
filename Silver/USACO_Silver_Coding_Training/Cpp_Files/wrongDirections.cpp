#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <unordered_set>
#include <queue>
#include <unordered_map>

using namespace std;
struct coordinate{
    int x,y,direction;
};
unordered_set<string> positions;
string rotateT(coordinate origin, coordinate end){
    int x = (-end.x+origin.x) + origin.x; int y = (-end.y+origin.y)+origin.y;
    return to_string(x) + " " + to_string(y);
}
string rotateL(coordinate origin, coordinate end){
    int y = (end.x-origin.x) + origin.y; int x = (-end.y+origin.y)+origin.x;
    return to_string(x) + " " + to_string(y);
}
string rotateR(coordinate origin, coordinate end){
    int x = (end.y-origin.y) + origin.x; int y = (-end.x+origin.x)+origin.y;
    return to_string(x) + " " + to_string(y);
}
int main() {
    string in; cin >> in; int N = in.size();
    coordinate instructions [N];
    coordinate current; current.x =0; current.y = 0; current.direction = 0;
    int direction = 0;
    // 0 = up
    // 1 = right
    // 2 = down
    // 3 = left
    int numF [100000] = {0};
    int count = 0;
    for(int i = 0; i < N; i++){
        if(in[i] == 'F'){
            count++;
            current.direction = direction;
            if(direction == 0){
                current.y++;
                instructions[i] = current;
            }
            if(direction == 1){
                current.x++;
                instructions[i] = current;
            }
            if(direction == 2){
                current.y--;
                instructions[i] = current;
            }
            if(direction == 3){
                current.x--;
                instructions[i] = current;
            }
        }
        else if(in[i] == 'R'){
            direction = (direction+1)%4;
            if(direction < 0){
                direction = 4+direction;
            }
            current.direction = direction;
            instructions[i] = current;
        }
        else if(in[i] == 'L'){
            direction = (direction-1)%4;
            if(direction < 0){
                direction = 4+direction;
            }
            current.direction = direction;
            instructions[i] = current;
        }
        numF[i] = count;
    }
    coordinate end = instructions[N-1];
    for(int i = 0; i < N;i++){
        if(in[i] == 'F'){
            coordinate next = end;
            coordinate origin = instructions[i];
            if(instructions[i].direction == 0){
               next.y--;
               origin.y--;
            }
            if(instructions[i].direction == 1){
                next.x--;
                origin.x--;
            }
            if(instructions[i].direction == 2){
                next.y++;
                origin.y++;
            }
            if(instructions[i].direction == 3){
               next.x++;
               origin.x++;
            }
            positions.insert(rotateL(origin,next));
            positions.insert(rotateR(origin,next));
        }
        else if(in[i] == 'R'){
            positions.insert(rotateT(instructions[i],end));
            if(numF[i] != count) {
                coordinate next = end;
                next.x = (-next.y + instructions[i].y) + instructions[i].x;
                next.y = (end.x - instructions[i].x) + instructions[i].y;
                if (instructions[i].direction == 1) {
                    string curr;
                    curr += to_string(next.x) + " " + to_string(next.y + 1);
                    positions.insert(curr);
                }
                if (instructions[i].direction == 2) {
                    string curr;
                    curr += to_string(next.x + 1) + " " + to_string(next.y);
                    positions.insert(curr);
                }
                if (instructions[i].direction == 3) {
                    string curr;
                    curr += to_string(next.x) + " " + to_string(next.y - 1);
                    positions.insert(curr);
                }
                if (instructions[i].direction == 0) {
                    string curr;
                    curr += to_string(next.x - 1) + " " + to_string(next.y);
                    positions.insert(curr);
                }
            }
            else{
                coordinate next = end;
                if (instructions[i].direction == 1) {
                    string curr;
                    curr += to_string(next.x) + " " + to_string(next.y + 1);
                    positions.insert(curr);
                }
                if (instructions[i].direction == 2) {
                    string curr;
                    curr += to_string(next.x + 1) + " " + to_string(next.y);
                    positions.insert(curr);
                }
                if (instructions[i].direction == 3) {
                    string curr;
                    curr += to_string(next.x) + " " + to_string(next.y - 1);
                    positions.insert(curr);
                }
                if (instructions[i].direction == 0) {
                    string curr;
                    curr += to_string(next.x - 1) + " " + to_string(next.y);
                    positions.insert(curr);
                }
            }
        }
        else if(in[i] == 'L') {
            positions.insert(rotateT(instructions[i], end));
            if (numF[i] != count) {
                coordinate next = end;
                next.x = (next.y - instructions[i].y) + instructions[i].x;
                next.y = (-end.x + instructions[i].x) + instructions[i].y;
                if (instructions[i].direction == 3) {
                    string curr;
                    curr += to_string(next.x) + " " + to_string(next.y + 1);
                    positions.insert(curr);
                }
                if (instructions[i].direction == 0) {
                    string curr;
                    curr += to_string(next.x + 1) + " " + to_string(next.y);
                    positions.insert(curr);
                }
                if (instructions[i].direction == 1) {
                    string curr;
                    curr += to_string(next.x) + " " + to_string(next.y - 1);
                    positions.insert(curr);
                }
                if (instructions[i].direction == 2) {
                    string curr;
                    curr += to_string(next.x - 1) + " " + to_string(next.y);
                    positions.insert(curr);
                }
            }
            else{
                coordinate next = end;
                if (instructions[i].direction == 3) {
                    string curr;
                    curr += to_string(next.x) + " " + to_string(next.y + 1);
                    positions.insert(curr);
                }
                if (instructions[i].direction == 0) {
                    string curr;
                    curr += to_string(next.x + 1) + " " + to_string(next.y);
                    positions.insert(curr);
                }
                if (instructions[i].direction == 1) {
                    string curr;
                    curr += to_string(next.x) + " " + to_string(next.y - 1);
                    positions.insert(curr);
                }
                if (instructions[i].direction == 2) {
                    string curr;
                    curr += to_string(next.x - 1) + " " + to_string(next.y);
                    positions.insert(curr);
                }
            }
        }
    }
    cout << positions.size();
    return 0;
}