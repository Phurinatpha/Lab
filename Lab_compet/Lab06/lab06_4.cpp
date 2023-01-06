#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    string id;
    cin >> id;
    
    if (next_permutation(id.begin(), id.end())){
        cout << id << endl;
    } else {
        cout << "No Successor" << endl;
    }
}