#include<iostream>
#include<set>
using namespace std;
int main(){
    // Set with values
    set<int, greater<int>> s1 = {6, 10, 5, 1};
    // Iterator for the set
    set<int> :: iterator it;
    // Print the elements of the set
    for(it=s1.begin(); it != s1.end();it++)
        cout<<*it<<" ";
    cout<<endl;
}

