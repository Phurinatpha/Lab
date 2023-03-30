#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);

    int N, Q, S, T, K;
    char c;

    scanf("%d %d\n", &N, &Q);
    vector<int> cows(N);

    for (int i = 0; i < N; i++)
    {
        scanf("%d\n", &cows[i]);
    }

    sort(cows.begin(), cows.end());

    for (int i = 0; i < Q; i++)
    {

        scanf("%c", &c);

        if (c == 'M')
        {
            int i, X;
            scanf("%d %d\n", &i, &X);
            cows[i - 1] = X;
            // After updating the weight of a cow, we need to sort the array again.
            sort(cows.begin(), cows.end());
        }
        else
        {

            scanf("%d %d %d\n", &S, &T, &K);

            int count = 0;
            int left = 0, right = N - 1;

            while (left <= right)
            {
                int mid = (left + right) / 2;
                if (cows[mid] <= K)
                {
                    count = mid - left + 1;
                    left = mid + 1;
                }
                else
                {
                    right = mid - 1;
                }
            }

            printf("%d\n", count);
        }
    }

    return 0;
}
