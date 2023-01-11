#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int a,b,c,z;
    cin >> a >> b >> c;
    
    for (int x=-c; x<a/2; x++){
        for (int y=x ;y<=a/2; y++){
            z = a-x-y;
            if (x*y*z == b){
                if (x*x+y*y+z*z == c){
                    cout << x << " " << y << " " << z;
                    return 0;
                }
            }
        }
    }
    cout << "No solution.";
    return 0;


}