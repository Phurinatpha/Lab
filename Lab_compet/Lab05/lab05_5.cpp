#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,t,com,max_ce;
    cin >> n >> t;
    int arr[n];
    for (int i = 0; i < n; i++){
        cin >> arr[i];
        
    }
    
    int i=0,j=0;
    for (int k = 0; k < t; k++){   
        cin >> com;
        if (com == 1){
            cin >> i >> j;
            if (i <= n and j >= arr[i])
                arr[i-1] += 1;
            else
                continue;
        } else if (com == 2){
            cin >> i >> j;
            if (i <= n and j<= arr[i])
                arr[i-1] -= 1;
            else
                continue;
        } else if (com == 3){
            cin >> i >> j;
            
        } else if (com == 4){
            cin >> i;
            if (i<=n){
                for (int i=0;i<n;i++){
                    if (arr[i] > 0)
                        arr[i]--;
                }
            } else
                continue;           
        }
        
        cout << endl;
        for (auto x:arr){
            cout << x << " ";
            
        }
    }

    
    return 0;
}

