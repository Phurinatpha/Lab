#include <bits/stdc++.h>
using namespace std;

void findMin(int V, vector<int>& denomination)
{
    // Sort denominations in decreasing order
    sort(denomination.rbegin(), denomination.rend());

    // Find minimum number of denominations
    vector<int> ans;
    for (int i = 0; i < denomination.size(); i++) {
        while (V >= denomination[i]) {
            ans.push_back(denomination[i]);
            V -= denomination[i];
        }
    }

    // Print result
    if (ans.size() == 0)
    {
        cout << "-1" << endl;
    }
    else
    {

        cout << ans.size() << endl;
    }
}

int main()
{
    int start, stop, n;
    cin >> start >> stop >> n;

    // Calculate value to be converted
    int V = abs(stop - start);

    // Input denominations
    vector<int> denomination(n);
    for (int i = 0; i < n; i++) {
        cin >> denomination[i];
    }

    findMin(V, denomination);

    return 0;
}
