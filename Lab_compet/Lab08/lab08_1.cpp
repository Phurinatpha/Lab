#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, m, q, t, l, r;
    string str, num;
    char Team, s;
    cin >> m;
    for (int i = 0; i < m; i++){
        cin >> t;
        cin >> num;
        for (int i = 0; i < t; i++){
            str += num;
        }   
    }
    
    n = str.length();
    cin >> q;

    for (int i = 0; i < q; i++){
        cin >> Team ;
        cin >> l >> r;
        if (Team == 'F'){
            for (int j = l; j <= r; j++){
                str.at(j) = '1';
            }
           
        } else if (Team == 'E') {
            for (int j = l; j <= r; j++) {
                str.at(j) = '0';
            }
           
        } else if (Team == 'I') {
            for (int j = l; j <= r; j++) {
                if(str[j] == '1'){
                    str.at(j) = '0';
                } else {
                    str.at(j) = '1';
                }
            }
        } else{
            int count = 0;
            for (int j = l; j <= r; j++){
                if(str[j]=='1'){
                    count++;
                }
            }
            cout << count << endl;
        }
    }
    
    return 0;
}