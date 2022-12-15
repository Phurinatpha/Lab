#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,th_pt = 1,i = 0;
    cin >> n;
    while (th_pt <n){
        th_pt *=2;
        i++;
    }
    cout << i+1 <<endl;

    return 0;
}