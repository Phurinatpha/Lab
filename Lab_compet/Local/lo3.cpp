#include<bits/stdc++.h> 
using namespace std;

long long fact(int n){
     long long result = 1;
     for (int i = 1; i <= n; i++) {
         result *= i;
     }
     return result;
}

int main() {
    int n;
    cin >> n;
    double ans = (double)fact(n)*((1/(double)fact(n-5)) - 1/(double)fact(n-4) + 1/(double)fact(n-3) - 1/(double)fact(n-2) + 1/(double)fact(n-1)-(1/(double)fact(n)));

    cout << (int)ans % ((int)pow(10, 7) + 7);

    return 0;
}
