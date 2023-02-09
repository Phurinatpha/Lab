#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    long long n,ch; 


    for (int i=0;i<10;i++){
        cin >> n;
        ch = n/2 + n/3 + n/4;
        cout << max(ch,n)<< endl;
    }
    
    
    return 0;
}

