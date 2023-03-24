#include <iostream>
using namespace std;

int main () {
    long long n , m;
    // scanf("%d %d", &n, &m);
    cin >> n;
    cin >> m;
        long long c[n+1];
    c[0] = 0;
    for(int i = 1; i <= n; i++){
        if (i > m) {
            c[i] = c[i-1] + c[i-m]; 
        } else if (i < m) {
            c[i] = 1;
        } else {
            c[i] = 2;
        }
    }
    cout << c[n];
    
}