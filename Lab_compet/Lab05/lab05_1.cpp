#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,sum_n = 0,co = 0;
    cin >> n;
    int arr[n];
    for (int i = 0; i<n; i++){
        cin >> arr[i];
    }

    sum_n = accumulate(arr, arr+n, sum_n)/float(n);
    
    for (int i = 0; i<n; i++){
        if (arr[i] < sum_n){
            co += sum_n - arr[i];
        }
    }
    
    cout << co;

    return 0;
}
