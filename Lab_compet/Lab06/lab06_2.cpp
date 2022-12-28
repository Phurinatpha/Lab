#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, m, a,res = 0,match = 0,j = 0;
    cin >> n >> m;
    n = (int)pow(2, n);
    int arr[n];
    memset(arr, 0, sizeof(arr));

    for (int i = 0; i < m; i++){
        cin >> a;
        arr[a - 1] = 1;
    }

    while (n > 0){
        for (int i = 0; i < n; i += 2){
            match = arr[i] + arr[i + 1];
            if (match == 0){
                arr[j] = 0;
            } else if (match == 1){
                res += 1;
                arr[j] = 0;
            } else if (match== 2){
                arr[j] = 1;
            }
            j++;
        }
        j = 0;
        n /= 2;
    }

    cout << res << endl;

    return 0;
}