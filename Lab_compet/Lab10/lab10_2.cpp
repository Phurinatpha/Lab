#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

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
        if(used == (1<<10)-1)
            cout << abcde << " / " << fghij << " = " << N << endl;
        else
            cout << "There are no solutions for N";
    return 0;
}
