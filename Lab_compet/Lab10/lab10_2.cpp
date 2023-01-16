#include <bits/stdc++.h>
#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    bool found = false;
    for(int fghij = 1234; fghij <= 98765/n; fghij++){
        int abcde = fghij * n;
        int temp, used = (fghij < 10000);
        temp = abcde;
        while (temp) {
            used = used | 1 << (temp % 10);
            temp = temp / 10;
        }
        temp = fghij;
        while (temp) {
            used = used | 1 << (temp % 10);
            temp = temp / 10;
        }
        if (used == (1 << 10) - 1) {
            found=true;
            printf("%05d / %05d = %d\n", abcde, fghij, n);
        }
       
    }

    if (!found) {
        cout << "There are no solutions for N." << endl;
    }
    
    return 0;
}