#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int k;
    cin >> k;
    int s[k];
    for (int i=0;i<k;i++){
        cin >> s[i];
        
    } 

    for (int a = 0; a< k - 5; a++)
        for (int b = a+1; b < k-4; b++)
            for (int c = b+1; c < k-3; c++)
                for (int d = c+1; d < k-2; d++)
                    for (int e = d+1; e < k-1; e++)
                        for (int f = e+1; f < k; f++)
                            // printf("%d %d %d %d %d %d\n", s[a],s[b],s[c],s[d],s[e],s[f]);
                            cout << s[a] << " " << s[b] << " " << s[c] << " " << s[d] << " " << s[e] << " " << s[f] << endl;
                            

    return 0;
}
