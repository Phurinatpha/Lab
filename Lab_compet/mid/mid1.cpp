#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,m,be,end; 
    char a;
    cin >> n >> m;
    int prefixSum[n];
    int arr[n];
    
    for (int i=0;i<n;i++){
        cin >> arr[i];
    }
    
    for (int k=0;k<m;k++){
        cin >> a;
        if (a == 'C'){
            cin  >> be >> end;
            arr[be-1] = end;
        }else if (a == 'P'){
            cin  >> be >> end;
            prefixSum[0] = arr[0];
            for (int i = 1; i < n; i++)
                prefixSum[i] = prefixSum[i - 1] * arr[i];
            // cout << "prefix " << prefixSum[end-1] << "\n";
            if (prefixSum[end-1] == 0)
                cout << '0';
            else if (prefixSum[end-1] > 0)
                cout << '+';
            else 
                cout << '-';
        }else {
            cout << "Shit";
        }
        
    }
    
    // for (auto i:prefixSum){
    //     cout << i << "\n";
    // }
    return 0;
}

