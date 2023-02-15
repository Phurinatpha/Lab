#include<bits/stdc++.h>
#define N 8

using namespace std;

int x[N];
int n = 8, mandatoryRow, mandatoryColumn;

bool place(int k, int i) 
{
    for (int j = 1; j <= k - 1; j++)
    {
        if ((x[j] == i) || (abs(x[j] - i) == abs(j - k)))
        {
            return false;
        }
    }
    return true;
}

void nQueens(int k) 
{
    for (int i = 1; i <= n; i++) 
    {
        if (place(k, i)) 
        {
            x[k] = i;
            if (k == n) 
            {
                cout << "Solution " << k << ": ";
                for (int j = 1; j <= n; j++) 
                {
                    cout << x[j] << " ";
                }
                cout << endl;
            }
            else 
            {
                nQueens(k + 1);
            }
        }
    }
}

int main() 
{
    cout << "Enter the mandatory queen's row: ";
    cin >> mandatoryRow;
    cout << "Enter the mandatory queen's column: ";
    cin >> mandatoryColumn;
    x[mandatoryRow] = mandatoryColumn;
    nQueens(1);
    return 0;
}
