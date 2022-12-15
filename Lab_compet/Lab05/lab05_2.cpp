#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s,word;
    getline(cin, s);
  
    stringstream iss(s);
    while (iss >> word){
        reverse(word.begin(),word.end());
        cout << word << " ";
    }

    return 0;
}
