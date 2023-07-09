#include <bits/stdc++.h>
using namespace std;

bool runround(int a) {

    int i,j,p,length,count=0;
    int s[20],checker[20],uniquecheck[10];
   
    for (i=0;i<10;i++) uniquecheck[i]=0;
    for (i=0;a!=0;i++){
        s[i]=a%10;
        a/=10;
        if (uniquecheck[s[i]]==0) uniquecheck[s[i]]=1; else return false;
        }
    length=i;
   
    p=length-1; 
    for (i=0;i<length;i++) checker[i]=0;
    while(count<length){
          int temp=s[p];
          for (j=0;j<temp;j++)
              {if (p==0) p=length-1; else p--;}
          if (checker[p]==1) return 0;
          checker[p]=1;
          count++;
          }
    return true;
}

int main() {
    int n;
    cin >> n;
    for (int i=0;i<n;i++){
        int N;
        cin >> N;
        N++;
        while(!runround(N)) N++;
        cout << N << endl;
    }

    return 0;
}