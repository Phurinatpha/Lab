#include <bits/stdc++.h>
using namespace std;

int maxContiguousSum(int A[], int n){
    int j;
    int max_so_far = A[0];
    int curr_max = A[0];
    for (j = 1; j < n; j++){
        curr_max = max(curr_max + A[j] , A[j]);
        max_so_far = max(curr_max, max_so_far );
    }
    return max_so_far;
}

int main(){
    int n;
    cin >> n;
    int arr[n];
    for (int i=0;i<n;i++){
        cin >> arr[i];
    }
    
    cout << maxContiguousSum(arr,n);

    return 0;
}