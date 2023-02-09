#include <bits/stdc++.h>
using namespace std;

void maxSubArraySum(int a[], int size)
{

    int max_so_far = INT_MIN, max_end_here = 0, start = 0, end = 0, s = 0;

    for (int i = 0; i < size; i++)
    {
        max_end_here += a[i];
        if (max_so_far <= max_end_here)
        {
            max_so_far = max_end_here;
            start = s;
            end = i;
        }

        if (max_end_here < 0)
        {
            max_end_here = 0;
            s = i + 1;
        }
    }
    if (max_so_far < 0){
        cout << "no";
        return;
    }

    cout << start + 1 << " " << end + 2;
}

int main(){
    int n;
    cin >> n;
    int arr[n-1];
    for (int i=0;i<n-1;i++){
        cin >> arr[i];
    }
    
    maxSubArraySum(arr,n-1);

    return 0;
}