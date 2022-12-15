#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s;
    cin >> s;
    list<char> l;
    list<char>::iterator cursur = l.begin();
    
    for (int i = 0;i<s.size();i++){
        if (s[i] == '['){
            cursur = l.begin();
        } else if (s[i] == ']'){
            cursur = l.end();
        } else{
            l.insert(cursur,s[i]);
        }
    }

    for (auto i:l)
        cout << i << "";

    return 0;
}
