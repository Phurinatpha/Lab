#include <bits/stdc++.h>
using namespace std;

int dr[] = {1,1,0,-1,-1,-1, 0, 1};
int dc[] = {0,1,1, 1, 0,-1,-1,-1};
char grid[99][99];

int floodfill(int r, int c, char c1, char c2, int rows ,int cols) {
    if (r < 0 || r >=  rows || c < 0 || c >= cols) return 0;
    if (grid[r][c] != c1) return 0;

    int ans = 1; 
    grid[r][c] = c2;
    for (int d = 0; d < 8; d++)
        ans += floodfill(r + dr[d], c + dc[d], c1, c2,rows,cols);
    return ans;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string input,s,intin;
    int rows = 0, cols = 0;
    
    while (getline(cin, s)){
        if (s[0] == 'L' || s[0] == 'W'){
            input += s;
            rows = s.size();
            input += '\n';
            cols += 1;
        } else {
            intin += s;
            intin += '\n'
        }
        
    }
    
    cout << input;
    cout << intin;
    cout << "====================" << endl;
    cout << rows << " " << cols;
    
    intin = intin.replace(' ','');
    intin = intin.replace(' ','\n');

    // for (int i = 0; i < rows; i++) {
    //     for (int j = 0; j < cols; j++) {
    //         grid[i][j] = (input[i*(cols+1) + j]);
    //     }
    // }

    // for (int i = 0; i < rows; i++) {
    //     for (int j = 0; j < cols; j++) {
    //         cout << grid[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    // cout << "---------------";
    // int a,b;
    // // while (cin >> a >> b){
    // //     cout << floodfill(a, b, 'W', 'L', rows , cols);
    // // }
    // cout << floodfill(6, 4, 'W', 'L', rows , cols);

    return 0;
}