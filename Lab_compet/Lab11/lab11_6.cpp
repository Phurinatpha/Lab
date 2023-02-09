#include <bits/stdc++.h>
using namespace std;
 
vector<vector<int> > result;
vector<vector<int> > res;
int co = 0;
bool isSafe(vector<vector<int>> board, int row, int col){
    int i, j;
    int N = board.size();
 
    for (i = 0; i < col; i++)
        if (board[row][i])
            return false;
 
    for (i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return false;
 
    for (i = row, j = col; j >= 0 && i < N; i++, j--)
        if (board[i][j])
            return false;
 
    return true;
}
 

bool solveNQUtil(vector<vector<int> >& board, int col){
    int N = board.size();
    
    if (col == N) {
        vector<int> v;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == 1)
                    v.push_back(j + 1);
            }
        }
        if (co < 4)
            result.push_back(v);
            co++;

        return true;
    }
    
    bool res = false;
    for (int i = 0; i < N; i++) {
        if (isSafe(board, i, col)) {
            board[i][col] = 1;
            res = solveNQUtil(board, col + 1) || res;
            board[i][col] = 0;
        }
    }
 
    return res;
}
 
vector<vector<int> > nQueen(int n,int r,int c){
    result.clear();
    co=0;
    vector<vector<int>> board(n, vector<int>(n, 0));
    if (solveNQUtil(board, r-1) == false) {
        return {};
    }
    
    sort(result.begin(), result.end());
    return result;
}

int main(){
    int n = 8;
    int t,r,c;
   
    cin >> t;
    cin >> r>>c;
    vector<vector<int>> v = nQueen(n,r,c);
    for (auto ar : v) {
        int co=0;
        for (auto it : ar)
            cout << it << " ";
        cout << "\n";
    }

    return 0;
}
