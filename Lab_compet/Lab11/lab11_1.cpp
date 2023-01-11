#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, m, num, be;
    cin >> n;
    int arr_n[n];
    vector<int> sum;
    
    for (int i = 0; i < n; i++){
        cin >> arr_n[i];
    }

    for (int i = 0; i < n; i++){
        for (int j = i + 1; j < n; j++){
            sum.push_back(arr_n[i] + arr_n[j]);
        }
    }

    cin >> m;
    while (m--){
        cin >> num;
        int min_m = 0;
        min_m = abs(sum.front() - num);
        for (auto a:sum){ 
            if ( min_m > abs(a - num)){
                min_m = abs(a - num);
            } 
        }
        cout << min_m << endl;        
    }
    

    return 0;
}