#include <iostream>
using namespace std;
 
long long count(string X, string Y)
{
    long long m = X.size();
    long long n = Y.size();
 
    long long T[m + 1][n + 1];
 
    for (long long i = 0; i <= m; i++) {
        T[i][0] = 1;
    }
 
    for (long long j = 1; j <= n; j++) {
        T[0][j] = 0;
    }

 
    for (long long i = 1; i <= m; i++)
    {
        for (long long j = 1; j <= n; j++) {
            T[i][j] = ((X[i - 1] == Y[j - 1]) ? T[i - 1][j - 1] : 0) + T[i - 1][j];
        }
    }
 
    return T[m][n];
}
 
int main()
{
    string X;   
    string Y;          
    cin >> X >> Y;
    cout << count(X, Y);
 
    return 0;
}