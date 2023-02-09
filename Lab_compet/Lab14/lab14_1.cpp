#include <bits/stdc++.h>
using namespace std;

bool partition (int arr[], int n){
	int sum = 0;
	int i, j;

	for (i = 0; i < n; i++)
	    sum += arr[i];

	if (sum % 2 != 0)
	    return false;

	bool part[n + 1][sum / 2 + 1];

	for (i = 0; i <= sum/2; i++)
        part[0][i] = false;

	for (i = 0; i <= n; i++)
	    part[i][0] = true;

	for (i = 1; i <= n; i++){
		for (j = 1; j <= sum/2; j++){
			part[i][j] = part[i-1][j];
			if (j >= arr[i - 1])
			part[i][j] = part[i][j] || part[i - 1][j - arr[i -1]];
		}
	}

	return part[n][sum/2];
}

int main(){
    int n;
    cin >>n;
	int arr[n];
    for (int i=0;i<n;i++)
        cin >> arr[i];
	
	if (partition(arr, n) == true)
		cout << "YES";
	else
		cout << "NO";
	return 0;
}
