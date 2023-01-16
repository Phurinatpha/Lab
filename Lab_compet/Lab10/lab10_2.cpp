#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int abcde,fghij;
    int temp, used = (fghij < 10000);
    
    temp=abcde;
    while(temp){
        used = used | 1<<(temp%10);
        temp = temp/10;
    }

    temp=fghij;
    while(temp){
        used = used | 1<<(temp%10);
        temp = temp/10;
    }

    if(used = (1<<10)-1)
        printf("%0.5d/ %0.5d = %d", abcde, fghij,N);
    
    return 0;
}
