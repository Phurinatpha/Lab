#include<bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string n;
    cin >> n;
    int row = 0,c = 0,count = 0,i = 0;
    char arr[1000];
    
    while (i < n.length()){
        if(i == 0){
            count += 1;
            row++;
            arr[i] = n[i];
        } else{
            for (int j = 0; j < row; j++){
                if(arr[j] >= n[i]){
                    arr[j] = n[i];
                    c++;
                    break;
                }
            } if (c != 1){
                arr[row] = n[i];
                row++;
                count += 1;
            } else
                c = 0;
        }
        i++;
    }

    cout << count;
    return 0;
}