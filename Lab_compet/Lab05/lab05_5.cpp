#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,t,com;
    cin >> n >> t;
    int arr[n];
    int result[n];
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }

    int i=0,j=0;
    for (int k = 0; k < t; k++){   
        cin >> com;
        if (com == 1){
            cin >> i >> j;
            if (i <= n && j > arr[i-1])
                arr[i-1] += 1;
        } 
        else if (com == 2){
            cin >> i >> j;
            if (i <= n && j <= arr[i-1])
                arr[i-1] -= 1;
        } 
        else if (com == 3){
            cin >> i >> j;
            // left
            if(i == 1){
                //No. == I
                if(arr[i-1] <= j - 2){
                    arr[i-1] = arr[i-1];
                }
                else if(arr[i-1] == j - 1){
                    arr[i-1] -= 1;
                }
                else if(arr[i-1] == j){
                    arr[i-1] -= 2;
                }
                else{
                    arr[i-1] -= 3;
                }
                //No. == I + 1
                if(arr[i] <= j - 2){
                    arr[i] = arr[i];
                }
                else if(arr[i] == j - 1){
                    arr[i] -= 1;
                }
                else if(arr[i] == j){
                    arr[i] -= 2;
                }
                else{
                    arr[i] -= 3;
                }
            }
            //right
            else if(i == n){
                if(arr[i-2] <= j - 2){
                    arr[i-2] = arr[i-2];
                }
                else if(arr[i-2] == j - 1){
                    arr[i-2] -= 1;
                }
                else if(arr[i-2] == j){
                    arr[i-2] -= 2;
                }
                else{
                    arr[i-2] -= 3;
                }
                if(arr[i-1] <= j - 2){
                    arr[i-1] = arr[i-1];
                }
                else if(arr[i-1] == j - 1){
                    arr[i-1] -= 1;
                }
                else if(arr[i-1] == j){
                    arr[i-1] -= 2;
                }
                else{
                    arr[i-1] -= 3;
                }
            }
            //middle
            else if(i < n){
                if(arr[i-2] <= j - 2){
                    arr[i-2] = arr[i-2];
                }
                else if(arr[i-2] == j - 1){
                    arr[i-2] -= 1;
                }
                else if(arr[i-2] == j){
                    arr[i-2] -= 2;
                }
                else{
                    arr[i-2] -= 3;
                }
                if(arr[i-1] <= j - 2){
                    arr[i-1] = arr[i-1];
                }
                else if(arr[i-1] == j - 1){
                    arr[i-1] -= 1;
                }
                else if(arr[i-1] == j){
                    arr[i-1] -= 2;
                }
                else{
                    arr[i-1] -= 3;
                }
                if(arr[i] <= j - 2){
                    arr[i] = arr[i];
                }
                else if(arr[i] == j - 1){
                    arr[i] -= 1;
                }
                else if(arr[i] == j){
                    arr[i] -= 2;
                }
                else{
                    arr[i] -= 3;
                }
            }
            else{
                arr[i] = arr[i];
            }
        } 
        else if (com == 4){
            cin >> j;
            if(j > 0){
                for (int l = 0;l < n;l++){
                    if (arr[l] >= j){
                        arr[l] -= 1;
                    }
                }
            }
            else{
                arr[i] = arr[i];
            }
        }
        for (auto x:arr){
            cout << x << " ";
        }
        cout << "\n";
    }

    return 0;
}
