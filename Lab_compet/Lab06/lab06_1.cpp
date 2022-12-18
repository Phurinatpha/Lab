#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    long long sum=0,t,a,n;
    cin >> n;
    priority_queue<long long,vector<long long>,greater<long long>> q;
    
    for (int i=0;i<n;i++){
        cin>>a;
        q.push(a);
    }

    while (q.size()>1){
        t = q.top();
        q.pop();
        t += q.top();
        q.pop();
        sum += t;
        q.push(t);
    }
    cout << sum;
    return 0;
}
