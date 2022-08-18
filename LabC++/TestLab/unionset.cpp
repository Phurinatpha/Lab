#include<iostream>
#include<set>
using namespace std;

template <typename T>
void getUnion(set<T> &a, set<T> b){
    typename set<T>::iterator itb;
    for(itb = b.begin(); itb != b.end(); itb++){
        a.insert(*itb);
    }
}

template <typename T>
set<T> getIntersection(set<T> a, set<T> b){
    set<T> result;
    typename set<T>::iterator ita;
    for(ita = a.begin(); ita != a.end(); ita++){
        if(b.find(*ita)!=b.end()){
            result.insert(*ita);
        }
    }
    return result;
}

template <typename T>
set<T> getDiffer(set<T> a, set<T> b){
    set<T> result,un,in;
    getUnion(a,b);
    typename set<T>::iterator itb;
    for(itb = b.begin(); itb != b.end(); itb++){
        if(a.find(*itb)!=a.end()){
            a.erase(*itb);
        }
    }
    return result=a;
}

int main(){
    // Set with values
    set<int> a,b,re,dif;
    // Iterator for the set
    set<int> :: iterator it;
    a = {1,2,3,4};
    b = {4,5,6};
    // getUnion(a,b);
    // // Print the elements of the set
    // for(it=a.begin(); it != a.end();it++)
    //     cout<<*it<<" ";
    // cout<<"\n";
    // re = getIntersection(a,b);
    // // Print the elements of the set
    // for(it=re.begin(); it != re.end();it++)
    //     cout<<*it<<" ";

    dif = getDiffer(a,b);
    for(it=dif.begin(); it != dif.end();it++)
        cout<<*it<<" ";
    
    cout<<endl;
}

