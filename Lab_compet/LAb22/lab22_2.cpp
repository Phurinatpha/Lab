#include <iostream>
using namespace std;
 
long countWays(long n)
{
    long A[n + 1];
    A[0] = 1, A[1] = 0, B[0] = 0, B[1] = 1;
    for (long i = 2; i <= n; i++) {
        A[i] = A[i - 2] + 2 * B[i - 1];
        B[i] = A[i - 1] + B[i - 2];
    }
 
    return A[n];
}
 

int main()
{
    long t,n;
    cin >> t;
    long ar[t];
    for (int i=0;i<t;i++){
        
        cin >> ar[i];
        
    }

    for (auto a:ar){
        cout << countWays(a) << endl;
    }
    return 0;
}