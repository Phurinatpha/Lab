#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);

    int N, Q, S, T, K;
    char c;

    scanf("%d %d\n", &N, &Q);
    int cows[N];

    for (int i = 0; i < N; i++)
    {
        scanf("%d\n", &cows[i]);
    }

    for (int i = 0; i < Q; i++)
    {

        scanf("%c", &c);

        if (c == 'M')
        {
            int i, X;
            scanf("%d %d\n", &i, &X);
            cows[i - 1] = X;
        }
        else
        {

            scanf("%d %d %d\n", &S, &T, &K);

            int count = count_if(cows + S - 1, cows + T, [K](int x)
                                 { return x <= K; });

            printf("%d\n", count);
        }
    }

    return 0;
}